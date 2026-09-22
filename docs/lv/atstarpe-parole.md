# Atstarpe parolē: mīts un realitāte

## Īsā atbilde

Atstarpe ir pilnvērtīga paroles rakstzīme. Tā var būt noderīga, jo palīdz veidot garas paroļu frāzes. Tā **nav** maģisks simbols, kas vāju paroli pēkšņi padara stipru.

## Ko saka NIST

Pašreizējā NIST SP 800-63B vadlīnija norāda, ka verificētājiem jāpieņem drukājamās ASCII rakstzīmes **un atstarpe**, jāatbalsta vismaz 64 rakstzīmju paroles, nav jāuzspiež kompozīcijas prasības un nav jāprasa patvaļīga periodiska paroļu maiņa. Pielikumā arī skaidrots, ka atkārtotas atstarpes dod maz papildu efektīvās drošības.

## Kas patiesībā ir svarīgi

- garums;
- neparedzamība;
- unikalitāte katram kontam;
- personisku faktu un paredzamu šablonu neizmantošana;
- bieži lietotu un kompromitētu paroļu bloķēšana;
- mēģinājumu ierobežošana un droša paroļu glabāšana pakalpojuma pusē;
- MFA/passkey, kur tas ir atbilstoši.

## Labs atstarpes lietojums

Atstarpe var palīdzēt veidot garu paroļu frāzi no savstarpēji nesaistītiem vārdiem. Arī tad frāzei jābūt grūti paredzamai un unikālai.

## Nepareiza interpretācija

Atstarpe pie `Password1!` nepadara šo paroli par stipru. Arī daudzas atkārtotas atstarpes neaizstāj labāku paroli.

## Avots

Skat. `nist_sp800_63b_4` failā [`../../data/sources.json`](../../data/sources.json).
