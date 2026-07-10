window.Step3DViewer = (() => {
  const BASE_GRAY_FILTER = "grayscale(1) brightness(0.84) contrast(1.18)";
  const NEON_DARK_FILTER =
    `${BASE_GRAY_FILTER} ` +
    "drop-shadow(0 0 2px rgba(81, 216, 183, 0.10))";
  const NEON_MAX_FILTER =
    `${BASE_GRAY_FILTER} ` +
    "drop-shadow(0 0 8px rgba(81, 216, 183, 0.84)) " +
    "drop-shadow(0 0 18px rgba(81, 216, 183, 0.56)) " +
    "drop-shadow(0 0 30px rgba(81, 216, 183, 0.34))";
  const DEFAULT_NEON_RAMP_MS = 750;

  function create(container, options = {}) {
    const element = typeof container === "string"
      ? document.querySelector(container)
      : container;

    if (!element) {
      throw new Error("Viewer container not found.");
    }

    let appearanceMode = "original";
    let spinRafId = null;
    let lastSpinTs = 0;
    let spinAngleRad = 0;
    let currentSpinSpeed = 0;
    let spinMode = "idle";
    let spinPhaseStartTs = 0;
    let spinPhaseDuration = 0;
    let spinSpeedFrom = 0;
    let spinSpeedTo = 0;
    let canvasBaseTransform = "";
    const MIN_SPIN_SPEED = 0.35;
    const MAX_SPIN_SPEED = 5.0;

    const viewer = new OV.EmbeddedViewer(element, {
      backgroundColor: new OV.RGBAColor(243, 245, 241, 0),
      defaultColor: new OV.RGBColor(166, 170, 176),
      edgeSettings: new OV.EdgeSettings(true, new OV.RGBColor(40, 48, 43), 35),
      onModelLoaded: () => {
        applyAppearanceMode(element, appearanceMode);
        if (typeof options.onModelLoaded === "function") {
          options.onModelLoaded();
        }
      },
      onModelLoadFailed: options.onModelLoadFailed
    });

    return {
      viewer,
      loadFromUrls: (urls) => viewer.LoadModelFromUrlList(normalizeList(urls)),
      loadFromFiles: (files) => viewer.LoadModelFromFileList(Array.from(files || [])),
      resize: () => viewer.Resize(),
      destroy: () => {
        stopSpinNow(element, false);
        viewer.Destroy();
      },
      setAppearanceMode: (mode) => {
        appearanceMode = mode === "neon" ? "neon" : "original";
        applyAppearanceMode(element, appearanceMode);
      },
      getAppearanceMode: () => appearanceMode,
      triggerNeonRamp: (durationMs) => {
        appearanceMode = "neon";
        animateNeonRamp(element, durationMs);
      },
      startIngestionSpin: (totalDurationMs) => {
        const safeDuration = Number.isFinite(totalDurationMs) ? Math.max(300, totalDurationMs) : 1200;
        beginSpinPhase("accelerate", safeDuration, MIN_SPIN_SPEED, MAX_SPIN_SPEED, element);
      },
      stopIngestionSpin: (decelerationMs) => {
        const safeDuration = Number.isFinite(decelerationMs) ? Math.max(220, decelerationMs) : 900;
        beginSpinPhase("decelerate", safeDuration, currentSpinSpeed, 0, element);
      }
    };

    function beginSpinPhase(phase, durationMs, fromSpeed, toSpeed, containerElement) {
      const canvas = containerElement.querySelector("canvas");
      if (!canvas) return;

      if (spinRafId === null) {
        canvasBaseTransform = canvas.style.transform || "";
      }
      canvas.style.transformOrigin = "50% 50%";

      if (spinRafId === null) {
        lastSpinTs = performance.now();
        spinRafId = requestAnimationFrame(stepSpin);
      }

      spinMode = phase;
      spinPhaseStartTs = performance.now();
      spinPhaseDuration = durationMs;
      spinSpeedFrom = Math.max(0, fromSpeed);
      spinSpeedTo = Math.max(0, toSpeed);
      currentSpinSpeed = spinSpeedFrom;
    }

    function stepSpin(now) {
      const canvas = element.querySelector("canvas");
      if (!canvas) {
        stopSpinNow(element);
        return;
      }

      const deltaSeconds = Math.max(0, (now - lastSpinTs) / 1000);
      lastSpinTs = now;

      const phaseProgress = spinPhaseDuration <= 0
        ? 1
        : Math.min(1, (now - spinPhaseStartTs) / spinPhaseDuration);

      if (spinMode === "accelerate") {
        const eased = 1 - Math.pow(1 - phaseProgress, 3);
        currentSpinSpeed = spinSpeedFrom + (spinSpeedTo - spinSpeedFrom) * eased;
      } else if (spinMode === "decelerate") {
        const eased = Math.pow(1 - phaseProgress, 2);
        currentSpinSpeed = spinSpeedTo + (spinSpeedFrom - spinSpeedTo) * eased;
      } else {
        currentSpinSpeed = 0;
      }

      spinAngleRad += currentSpinSpeed * deltaSeconds;
      const rotateTransform = `rotateZ(${spinAngleRad}rad)`;
      canvas.style.transform = canvasBaseTransform ? `${canvasBaseTransform} ${rotateTransform}` : rotateTransform;

      const finishedDecel = spinMode === "decelerate" && phaseProgress >= 1;
      if (finishedDecel) {
        stopSpinNow(element, true);
        return;
      }

      spinRafId = requestAnimationFrame(stepSpin);
    }

    function stopSpinNow(containerElement, keepFinalTransform) {
      if (spinRafId !== null) {
        cancelAnimationFrame(spinRafId);
      }
      spinRafId = null;
      spinMode = "idle";
      currentSpinSpeed = 0;
      const canvas = containerElement.querySelector("canvas");
      if (canvas) {
        if (keepFinalTransform) {
          const finalRotate = `rotateZ(${spinAngleRad}rad)`;
          canvas.style.transform = canvasBaseTransform ? `${canvasBaseTransform} ${finalRotate}` : finalRotate;
        } else {
          canvas.style.transform = canvasBaseTransform;
        }
      }
      canvasBaseTransform = "";
    }
  }

  function applyAppearanceMode(container, mode) {
    // Keep the surrounding frame neutral and apply appearance only to the rendered model canvas.
    const target = container.querySelector("canvas") || container;

    // Ensure no stale filter remains on the outer container.
    container.style.filter = "none";

    // Stop any previous filter animation before applying a new mode.
    container.getAnimations().forEach((animation) => animation.cancel());
    target.getAnimations().forEach((animation) => animation.cancel());

    if (mode === "neon") {
      animateNeonRamp(container, DEFAULT_NEON_RAMP_MS);
      return;
    }

    // Force a consistent neutral look independent of source model textures/colors.
    target.style.filter = BASE_GRAY_FILTER;
  }

  function animateNeonRamp(container, durationMs) {
    const target = container.querySelector("canvas") || container;
    const safeDuration = Number.isFinite(durationMs) ? Math.max(80, durationMs) : DEFAULT_NEON_RAMP_MS;
    target.getAnimations().forEach((animation) => animation.cancel());
    target.style.filter = NEON_DARK_FILTER;
    target.animate(
      [
        { filter: NEON_DARK_FILTER },
        { filter: NEON_MAX_FILTER },
      ],
      {
        duration: safeDuration,
        easing: "ease-out",
        fill: "forwards",
      }
    );
  }

  function normalizeList(value) {
    if (Array.isArray(value)) {
      return value.filter(Boolean);
    }

    return String(value || "")
      .split(",")
      .map((item) => item.trim())
      .filter(Boolean);
  }

  return { create };
})();
