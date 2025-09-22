# Rendszerterv

## A rendszer célja

Egy egyszerű weboldal létrehozása, ami egy gomb megnyomására kér egy viccet a backend adatbázístóé és megjeleníti a képernyőn. Továbbá ezt a viccet a felhasználó értékelheti és egy leader board oldalon megtekintheti a viccek értékelését.

---

## Projekt terv

### Projektszerepkörök, felelősségek
Frontend interface fejlesztő, Frontend Javascript fejlesztő, Backend python+flask fejlesztő, Backend adatbázis fejlesztő
### Projektmunkások és felelősségeik
Kondor Kristóf-Frontend interface fejlesztő, Sebestyén Bence-Backend python+flask fejlesztő, Kacsó Melinda-Backend adatbázis fejlesztő, Nyiri László-Frontend Javascript

---

## Üzleti folyamatok modellje

### Üzleti szereplők
Felhasználó
### Üzleti folyamatok
A felhasználó gombbal kérhet viccet és gombok segítségével értékelheti a viccet. 
### Üzleti entitások
Viccek adatbázis ami tartalmazza a viccet és értékelését.

---

## Követelmények

### Funkcionális követelmények
Vicc betöltése, vicc értékelése, viccek listázása értékelés szerint
### Nemfunkcionális követelmények
Jó olvashatóság több fajta méretü eszközön. Gyors betöltési idő

---

## Funkcionális terv

### Rendszerszereplők

### Rendszerhasználati esetek és lefutásaik

### Határosztályok

### Menü-hierarchiák

### Képernyőtervek

---

## Fizikai környezet

### Vásárolt softwarekomponensek és külső rendszerek

### Hardver és hálózati topológia

### Fizikai alrendszerek

### Fejlesztő eszközök

### Keretrendszer (pl. Spring)

A backend fejlesztéséhez a **Flask** keretrendszert használjuk, amely lehetővé teszi a gyors és egyszerű webes API-k fejlesztését. A Flask kezeli a viccek betöltését az adatbázisból, a felhasználói **like** és **dislike** értékelések tárolását, valamint a **toplista** dinamikus frissítését. Az alkalmazás RESTful API-t biztosít, amely lehetővé teszi a viccek és azok értékeléseinek lekérését, illetve az aktuális rangsor megjelenítését.

---

## Absztrakt domain modell

### Domain specifikáció, fogalmak

### Absztrakt komponensek, ezek kapcsolatai

---

## Architekturális terv

### Egy architekturális tervezési minta (pl. MVC, 3-rétegű alkalmazás, …)

### Az alkalmazás rétegei, fő komponensei, ezek kapcsolatai

### Változások kezelése

### Rendszer bővíthetősége

### Biztonsági funkciók

---

## Adatbázis terv

### Logikai adatmodell

### Tárolt eljárások

### Fizikai adatmodellt legeneráló SQL szkript

---

## Implementációs terv

### Perzisztencia-osztályok

### Üzleti logika osztályai

### Kliensoldal osztályai

---

## Tesztterv

---

## Telepítési terv

---

## Karbantartási terv
