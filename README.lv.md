# Paroļu drošība

**Latviski** · [English](README.md)

**Pierādījumos balstītas vadlīnijas lietotājiem, produktu komandām un pakalpojumu uzturētājiem.**

Repozitorijs nošķir **padomus lietotājam** no **prasībām pakalpojumam**. Angļu versija ir globāls pamata materiāls; latviešu versija ir lokalizēts skaidrojums Latvijas auditorijai, nevis apgalvojums, ka Latvijas regulējums nosaka globālu paroļu standartu.

> **Pamatprincips:** droša paroļu stratēģija nav simbolu recepte. Ja iespējams, dod priekšroku pret pikšķerēšanu noturīgai autentifikācijai; citādi izmanto garas, unikālas un neparedzamas paroles, paroļu pārvaldnieku un pakalpojuma puses kontroles, kas bloķē bieži lietotas vai kompromitētas paroles.

## Ko aptver projekts

- paroļu un paroļu frāžu ieteikumus cilvēkiem;
- paroļu pārvaldniekus un kontu atkopšanu;
- atstarpju nozīmi parolēs;
- mūsdienīgu pakalpojuma puses paroļu politiku;
- NIST SP 800-63B un OWASP ASVS 5.0 prasību skaidrojumu;
- passkey, MFA un paroļu ierobežojumus pret pikšķerēšanu.

## Atstarpe parolē

**Jā, atstarpei jābūt atļautai. Nē, atstarpe nav maģisks drošības simbols.** NIST pašreizējā vadlīnija iesaka paroļu verificētājiem pieņemt atstarpi un atbalstīt paroļu frāzes. Tā arī norāda, ka atkārtotu atstarpju pievienošana dod maz papildu efektīvās drošības. Drošību nosaka viss noslēpums — garums, neparedzamība, unikalitāte un autentifikācijas kontroles.

Skat. [Atstarpe parolē: mīts un realitāte](docs/lv/atstarpe-parole.md).

## Īsā versija

1. Ja iespējams, izmanto passkey vai citu pret pikšķerēšanu noturīgu risinājumu.
2. Katram kontam izmanto citu paroli.
3. Izmanto paroļu pārvaldnieku.
4. Ja parole jāatceras pašam, izvēlies garu un neparedzamu paroļu frāzi.
5. Neuzskati atstarpi vai speciālo simbolu par maģisku drošības elementu.
6. Nemaini paroli tikai kalendāra dēļ.
7. Īpaši sargā galveno e-pastu un atkopšanas kanālus.
8. Ja ir aizdomas par kompromitāciju, nomaini paroli un, kur iespējams, atsauc vecās sesijas.

Pakalpojumu uzturētājiem: [Paroļu politika pakalpojumiem](docs/lv/pakalpojumu-politika.md).

## Pierādījumu modelis

`avots → apgalvojums → vadlīnija → validācija`

`data/guidance.*.json` apgalvojumi atsaucas uz `data/sources.json` avotu ID. CI pārbauda valodu paritāti, avotu atsauces un redakcionālās drošības nosacījumus.

## Svarīga nianse

NIST **15 rakstzīmju minimums** ir prasība verificētājam parolei, kas tiek izmantota kā **vienīgais autentifikācijas faktors**. Tas nav universāls apgalvojums, ka ikvienā kontekstā cilvēkam obligāti jāveido tieši 15+ rakstzīmju parole. Ja parole ir tikai viens no MFA faktoriem, NIST atļauj 8 rakstzīmju minimumu. Pakalpojumam vienlaikus jāatbalsta vismaz 64 rakstzīmes.

## Struktūra

- `docs/en/` — globālais angļu materiāls;
- `docs/lv/` — latviešu materiāls;
- `data/` — mašīnlasāmas vadlīnijas un avotu reģistrs;
- `scripts/` — validācija un saišu pārbaude;
- `tests/` — regresijas testi.

## Tvērums

Šis ir izglītojošs un inženiertehnisks materiāls, nevis juridisks atzinums vai kāda produkta sertifikācija.

## Autors

**Zigmārs Ancveirs** — tehnoloģiju vadītājs, programmatūras inženieris un neatkarīgs kiberdrošības pētnieks.

## Licence

Dokumentācija un dati: **CC BY 4.0**. Kods un automatizācija: **MIT**. Skat. [LICENSE.md](LICENSE.md).
