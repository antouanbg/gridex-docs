import assert from 'node:assert/strict';
import {readFileSync,readdirSync} from 'node:fs';
const bg='docs/';
const en='i18n/en/docusaurus-plugin-content-docs/current/';
const files=readdirSync(bg).filter(f=>f.endsWith('.md')).sort();
assert.deepEqual(files,readdirSync(en).filter(f=>f.endsWith('.md')).sort(),'BG/EN page parity');
for(const base of [bg,en])for(const file of files){
 const body=readFileSync(base+file,'utf8');
 assert(!/antouan|antuan|angelov|антуан|ангелов|github\.com\/antouanbg/i.test(body),base+file+': private project attribution');
 assert(!/Профил → Услуги|Profile → Services|Клиенти и договори|Customers [&] contracts|Users [&] invitations|Не се изпраща автоматичен имейл|No automatic email is sent/.test(body),base+file+': outdated instruction');
 if(file==='navigation-and-permissions.md')for(const anchor of ['menu-matrix','authority-matrix','role-actions','service-access','approval-flow'])assert(body.includes('{#'+anchor+'}'),anchor);
}
console.log('GUIDES_CONSISTENT: '+files.length+' BG/EN pairs; required matrices and obsolete-name checks passed.');
