(function initializeStepQI18n(global) {
  const messages = {
    de: {
      'app.title': 'STEP-Q Metadatenformular',
      'app.language': 'Sprache',
      'app.intro': 'Wähle zuerst die Produktart. Danach werden die passenden Eingabefelder aus der Spezifikation geladen.',
      'files.title': 'STEP-Dateien',
      'files.pick': 'Eine oder mehrere STEP-Dateien auswählen',
      'files.selectAll': 'Alle Dateien auswählen',
      'files.empty': 'Noch keine Dateien ausgewählt.',
      'files.applySelection': 'Aktuelle Spezifikationen auf Auswahl anwenden',
      'files.clearSelection': 'Auswahl aufheben',
      'form.basicTitle': 'Grund-Spezifikationen',
      'form.submit': 'STEP-Q Metadaten übernehmen',
      'form.skipAnimation': 'Animation überspringen',
      'form.yes': 'Ja',
      'viewer.title': 'STEP-Vorschau',
      'viewer.placeholder': 'STEP-Datei hier ablegen oder klicken.',
      'catalog.title': 'Auswahlkatalog',
      'catalog.close': 'Schließen',
      'catalog.search': 'Katalog durchsuchen',
      'catalog.add': 'Hinzufügen',
      'catalog.noResults': 'Keine Treffer.',
      'catalog.noDescription': 'Keine Beschreibung',
      'field.addQuantity': 'Menge angeben',
      'field.decimalExample': 'z. B. 2.5',
      'field.freeText': 'Freitext nur für dokumentierte Ausnahmen',
      'field.selectProductFirst': 'Erst Produktart wählen',
      'selection.clear': 'Auswahl löschen',
      'action.explain': 'Aktionen erklären',
      'action.edit': 'Bearbeiten',
      'action.discard': 'Löschen',
      'action.saveOriginal': 'Originaldatei mit STEP-Q überschreiben',
      'action.saveCopy': 'STEP-Q-Kopie erstellen (Original behalten)',
      'action.saveCopyButton': 'STEP-Q-Kopie speichern',
      'action.nextFile': 'Nächste Datei',
      'action.restart': 'Neu starten',
      'result.metadata': 'Metadaten anzeigen'
    },
    en: {
      'app.title': 'STEP-Q metadata form',
      'app.language': 'Language',
      'app.intro': 'Select a product type first. The relevant fields will then be loaded from the specification.',
      'files.title': 'STEP files',
      'files.pick': 'Select one or more STEP files',
      'files.selectAll': 'Select all files',
      'files.empty': 'No files selected yet.',
      'files.applySelection': 'Apply current specifications to selection',
      'files.clearSelection': 'Clear selection',
      'form.basicTitle': 'Basic specifications',
      'form.submit': 'Apply STEP-Q metadata',
      'form.skipAnimation': 'Skip animation',
      'form.yes': 'Yes',
      'viewer.title': 'STEP preview',
      'viewer.placeholder': 'Drop a STEP file here or click.',
      'catalog.title': 'Selection catalog',
      'catalog.close': 'Close',
      'catalog.search': 'Search catalog',
      'catalog.add': 'Add',
      'catalog.noResults': 'No results.',
      'catalog.noDescription': 'No description',
      'field.addQuantity': 'Enter quantity',
      'field.decimalExample': 'e.g. 2.5',
      'field.freeText': 'Free text for documented exceptions only',
      'field.selectProductFirst': 'Select a product type first',
      'selection.clear': 'Clear selection',
      'action.explain': 'Explain actions',
      'action.edit': 'Edit',
      'action.discard': 'Discard',
      'action.saveOriginal': 'Overwrite original file with STEP-Q',
      'action.saveCopy': 'Create STEP-Q copy (keep original)',
      'action.saveCopyButton': 'Save STEP-Q copy',
      'action.nextFile': 'Next file',
      'action.restart': 'Restart',
      'result.metadata': 'Show metadata'
    }
  };

  const products = {
    sheet: { de: 'Blech', en: 'Sheet metal' },
    tube: { de: 'Rohr/Profil', en: 'Tube/profile' },
    turning: { de: 'Drehteil', en: 'Turned part' },
    milling: { de: 'Frästeil', en: 'Milled part' }
  };

  const fieldLabels = {
    Q_PRODUCT_TYPE: { de: 'Produktart', en: 'Product type' },
    Q_QUANTITY: { de: 'Stückzahl', en: 'Quantity' },
    Q_MATERIAL: { de: 'Material', en: 'Material' },
    Q_THICKNESS: { de: 'Dicke', en: 'Thickness' },
    Q_MICRO_JOINTS: { de: 'Mikrosteg(e) entfernen?', en: 'Remove micro-tabs?' },
    Q_DEBURRING: { de: 'Entgraten', en: 'Deburring' },
    Q_EDGE_ROUNDING: { de: 'Kanten verrunden', en: 'Round edges' },
    Q_TEXT_ENGRAVING: { de: 'Gravuren', en: 'Engraving' },
    Q_SHEET_METAL_FIT_TYPE: { de: 'Passungen', en: 'Fits' },
    Q_QUANTITY_THREADS: { de: 'Gewinde', en: 'Threads' },
    Q_QUANTITY_EXTRUDED_THREADS: { de: 'Gewindedurchzüge', en: 'Extruded threads' },
    Q_QUANTITY_COUNTERSINKS: { de: 'Senkungen', en: 'Countersinks' },
    Q_CORNER_RELIEF: { de: 'Ecken freistellen', en: 'Corner relief' },
    Q_LEVELING: { de: 'Richten', en: 'Straightening' },
    Q_QUANTITY_WELDING_STUDS: { de: 'Bolzenschweißen', en: 'Welding studs' },
    Q_QUANTITY_PRESS_NUTS: { de: 'Einpressmuttern', en: 'Press nuts' },
    Q_CUTTING_TECHNOLOGY: { de: 'Schneidtechnologie', en: 'Cutting technology' },
    Q_TOP_SIDE: { de: 'Oberseite', en: 'Top side' },
    Q_ROLLING_DIRECTION: { de: 'Walzrichtung', en: 'Rolling direction' },
    Q_GALVANIZING: { de: 'Verzinken', en: 'Galvanizing' },
    Q_POWDER_COATING_APPLICATION: { de: 'Pulverbeschichtungsanwendung', en: 'Powder coating application' },
    Q_POWDER_COATING_GLOSS: { de: 'Pulverbeschichtungs-Glanzgrad', en: 'Powder coating gloss' },
    Q_POWDER_COATING_TEXTURE: { de: 'Pulverbeschichtungs-Textur', en: 'Powder coating texture' },
    Q_TEST_REPORT: { de: 'Abnahmeprüfzeugnis nach EN 10204', en: 'Inspection certificate according to EN 10204' },
    Q_SAMPLE_QUANTITY: { de: 'Musterteile', en: 'Sample parts' },
    Q_TUBE_LASER_CUTTING_METHOD: { de: 'Laserschnittverfahren', en: 'Laser cutting method' },
    Q_GENERAL_TOLERANCE_LENGTH_ANGLE: { de: 'Allgemeintoleranzen für Längen und Winkel', en: 'General tolerances for lengths and angles' },
    Q_GENERAL_TOLERANCE_SHAPE_POSITION: { de: 'Allgemeintoleranzen für Form und Lage', en: 'General tolerances for form and position' },
    Q_ADDITIONAL_TOLERANCE_IT_CLASS: { de: 'Weitere Toleranzen: IT-Klasse', en: 'Additional tolerances: IT class' },
    Q_ADDITIONAL_TOLERANCE_RANGE: { de: 'Weitere Toleranzen: Toleranzbereich', en: 'Additional tolerances: tolerance range' },
    Q_THREAD_TYPE: { de: 'Gewindeart', en: 'Thread type' },
    Q_SURFACE_FINISH: { de: 'Oberflächengüte', en: 'Surface finish' },
    Q_ANODIZING: { de: 'Eloxieren', en: 'Anodizing' },
    Q_BURNISHING: { de: 'Brünieren', en: 'Black oxide coating' }
  };

  const groups = {
    'Grund-Spezifikationen': { de: 'Grund-Spezifikationen', en: 'Basic specifications' },
    'Weiterbearbeitung': { de: 'Weiterbearbeitung', en: 'Further processing' },
    'Oberfläche': { de: 'Oberfläche', en: 'Surface' },
    'Zertifikate & Sonstiges': { de: 'Zertifikate & Sonstiges', en: 'Certificates & other' }
  };

  const enumLabels = {
    Q_POWDER_COATING_TEXTURE: {
      smooth: { de: 'Glatt', en: 'Smooth texture', titleEn: 'Smooth finish' },
      fine_texture: { de: 'Feinstruktur', en: 'Fine texture', titleEn: 'Fine finish' },
      texture: { de: 'Struktur', en: 'Structured texture', titleEn: 'Structured finish' },
      coarse_texture: { de: 'Grobstruktur', en: 'Coarse texture', titleEn: 'Coarse finish' }
    },
    Q_DEBURRING: {
      one_sided_rear: { de: 'Einseitig rückseitig entgraten', en: 'One-sided rear-side deburring', titleEn: 'One-sided rear' },
      two_sided: { de: 'Zweiseitig entgraten', en: 'Two-sided deburring', titleEn: 'Two-sided' },
      barrel_finish: { de: 'Trowalisieren / Gleitschleifen', en: 'Barrel finishing / tumbling', titleEn: 'Barrel finishing' },
      manual_rear: { de: 'Manuell rückseitig entgraten', en: 'Manual rear-side deburring', titleEn: 'Manual rear' }
    }
  };

  function translate(key, language = 'de', values = {}) {
    const template = messages[language]?.[key] ?? messages.de[key] ?? key;
    return template.replace(/\{(\w+)\}/g, (placeholder, name) => String(values[name] ?? placeholder));
  }

  function fieldLabel(fieldKey, language = 'de', fallback = '') {
    return fieldLabels[fieldKey]?.[language] ?? fallback;
  }

  function groupLabel(group, language = 'de', fallback = group) {
    return groups[group]?.[language] ?? fallback;
  }

  function productLabel(productType, language = 'de', fallback = productType) {
    return products[productType]?.[language] ?? fallback;
  }

  function enumLabel(enumName, value, language = 'de', fallback = value) {
    return enumLabels[enumName]?.[value]?.[language] ?? fallback;
  }

  function enumTitle(enumName, value, language = 'de', fallback = value) {
    const label = enumLabels[enumName]?.[value];
    return language === 'en' ? (label?.titleEn ?? fallback) : (label?.de ?? fallback);
  }

  const api = { translate, fieldLabel, groupLabel, productLabel, enumLabel, enumTitle };
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  global.STEPQ_I18N = api;
})(globalThis);
