# Paroļu politika pakalpojumiem

Šī lapa paredzēta produktu, identitātes un drošības komandām. Tā apraksta aizstāvamu pamata līmeni, kas balstīts NIST SP 800-63B un OWASP ASVS 5.0. Tā neaizstāj konkrētas sistēmas draudu modeli.

## Pamata prasības

1. Ja parole ir **vienīgais autentifikācijas faktors**, prasi vismaz **15 rakstzīmes**.
2. Ja parole ir tikai viens no MFA faktoriem, NIST atļauj īsāku minimumu, bet ne mazāk par **8 rakstzīmēm**.
3. Atļauj vismaz **64 rakstzīmes**.
4. Pieņem plašu rakstzīmju kopumu, tostarp **atstarpes**; patvaļīgi nesaīsini un nemaini reģistru.
5. Neprasi fiksētu lielo/mazo burtu, ciparu un simbolu kombināciju.
6. Atļauj ielīmēšanu, pārlūka paroļu palīgus un ārējos paroļu pārvaldniekus.
7. Bloķē bieži lietotas, paredzamas un kompromitētas paroles.
8. Neprasi periodisku paroļu rotāciju bez kompromitācijas pazīmēm.
9. Ierobežo mēģinājumus un aizsargājies pret automatizētu minēšanu un credential stuffing.
10. Glabā paroles ar piemērotu sālītu un skaitļošanas ziņā dārgu paroļu jaukšanas shēmu.
11. Piedāvā stiprāku autentifikāciju; ja risks to prasa, dod priekšroku pret pikšķerēšanu noturīgiem risinājumiem.

## Kāpēc tas ir svarīgi

Paroļu politika ir sistēmas kontrole, nevis pārbaudījums lietotāja spējai izpildīt simbolu mīklu. Labas pakalpojuma puses kontroles mazina paredzamu lietotāju uzvedību un ļauj paroļu pārvaldniekiem un paroļu frāzēm strādāt tā, kā paredzēts.

## Avoti

Skat. `nist_sp800_63b_4` un `owasp_asvs_5_v6_2` failā [`../../data/sources.json`](../../data/sources.json).
