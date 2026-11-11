const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const test = require('node:test');

const i18n = require('../step_q_i18n.js');
const formPath = path.join(__dirname, '..', 'step_q_form.html');
const formHtml = fs.readFileSync(formPath, 'utf8');

test('stable page keys return both locales', () => {
  assert.equal(i18n.translate('app.title', 'de'), 'STEP-Q Metadatenformular');
  assert.equal(i18n.translate('app.title', 'en'), 'STEP-Q metadata form');
  assert.equal(i18n.translate('files.pick', 'en'), 'Select one or more STEP files');
});

test('all semantic keys referenced by the form resolve in both locales', () => {
  const translationKeys = [...formHtml.matchAll(/data-i18n-key="([^"]+)"/g)].map(match => match[1]);
  const fieldKeys = [...formHtml.matchAll(/data-i18n-field-key="([^"]+)"/g)].map(match => match[1]);
  assert.ok(translationKeys.length > 0);
  assert.ok(fieldKeys.length > 0);
  for (const key of translationKeys) {
    assert.notEqual(i18n.translate(key, 'de'), key, `Missing German UI key: ${key}`);
    assert.notEqual(i18n.translate(key, 'en'), key, `Missing English UI key: ${key}`);
  }
  for (const key of fieldKeys) {
    assert.notEqual(i18n.fieldLabel(key, 'de'), '', `Missing German field key: ${key}`);
    assert.notEqual(i18n.fieldLabel(key, 'en'), '', `Missing English field key: ${key}`);
  }
});

test('field and group labels are keyed by STEP-Q field identifiers', () => {
  assert.equal(i18n.fieldLabel('Q_QUANTITY', 'de'), 'Stückzahl');
  assert.equal(i18n.fieldLabel('Q_QUANTITY', 'en'), 'Quantity');
  assert.equal(i18n.groupLabel('Weiterbearbeitung', 'en'), 'Further processing');
  assert.equal(i18n.productLabel('milling', 'en'), 'Milled part');
});

test('powder texture display is localized without changing its STEP-Q value', () => {
  const storedValue = 'texture';
  assert.equal(i18n.enumLabel('Q_POWDER_COATING_TEXTURE', storedValue, 'de'), 'Struktur');
  assert.equal(i18n.enumLabel('Q_POWDER_COATING_TEXTURE', storedValue, 'en'), 'Structured texture');
  assert.equal(storedValue, 'texture');
  assert.equal(i18n.enumTitle('Q_POWDER_COATING_TEXTURE', storedValue, 'en'), 'Structured finish');
});

test('unknown keys fall back to their identifier or supplied label', () => {
  assert.equal(i18n.translate('missing.key', 'en'), 'missing.key');
  assert.equal(i18n.fieldLabel('Q_UNKNOWN', 'en', 'Fallback'), 'Fallback');
});

test('form loads keyed translations before its inline application script', () => {
  const moduleIndex = formHtml.indexOf('<script src="./step_q_i18n.js"></script>');
  const inlineScriptIndex = formHtml.indexOf('<script>', moduleIndex + 1);
  assert.ok(moduleIndex >= 0, 'i18n module script is present');
  assert.ok(inlineScriptIndex > moduleIndex, 'i18n module loads before the form script');
  assert.match(formHtml, /data-i18n-key="app\.title"/);
  assert.match(formHtml, /data-i18n-key="files\.pick"/);
});
