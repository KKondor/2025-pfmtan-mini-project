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
Felhasználó, rendszeradminisztrátor
### Rendszerhasználati esetek és lefutásaik
1. Vicc kérése: A felhasználó gomb nyomására kér viccet, ami az oldal javascript segítségével kér a backend-től és az ad egy random viccet az adatbázisból.
2. Vicc értékelése: A felhasználó értékeli egy like vagy dislike gomb nyomására, az oldal ennek hatására jelez a backend-nek hogy az adatbázisban növelje vagy csökkentse az értékelés szintjét.
3. Vicc toplista: A felhasználó megtekinti a viccek listáját értékelés alapján csökkentve rendezve. Ezt a backend adatbázistól kéri le.
### Határosztályok
Ha nincs vicc, vagy nem fér hozzá az adatbázishoz az oldal akkor ezt hibával jelezzük a felhasználó felé.
### Menü-hierarchiák
A felhasználó először a main-page csatlakozik, ahol talál egy generálás gombot, a viccet, értékelési gombokat és egy hyperlinket a leaderboard-page -re. A leaderboard-page tartalmaz egy listát és egy hyperlinket vissza a main-page -re.

---

## Fizikai környezet

### Vásárolt softwarekomponensek és külső rendszerek

### Hardver és hálózati topológia

### Fizikai alrendszerek

### Fejlesztő eszközök

A projekt fejlesztéséhez az alábbi eszközöket és technológiákat használjuk:

- **Programozási nyelvek**:
  - **HTML/CSS**: A frontend megjelenítéséhez és dizájnhoz.
  - **JavaScript**: A dinamikus interakciók és az API-k kezelése a frontend oldalon.
  - **Python**: A backend logika, adatbázis-kezelés és API-k fejlesztéséhez.

- **Adatbázis**:
  
- **Verziókezelés**:
  - **Git**: A kód nyomon követésére és kezelésére, amely lehetővé teszi a csapat számára a párhuzamos munkát és a könnyű kódmegosztást.

### Keretrendszer (pl. Spring)

A backend fejlesztéséhez a **Flask** keretrendszert használjuk, amely lehetővé teszi a gyors és egyszerű webes API-k fejlesztését. A Flask kezeli a viccek betöltését az adatbázisból, a felhasználói **like** és **dislike** értékelések tárolását, valamint a **toplista** dinamikus frissítését. Az alkalmazás RESTful API-t biztosít, amely lehetővé teszi a viccek és azok értékeléseinek lekérését, illetve az aktuális rangsor megjelenítését.

---

## Absztrakt domain modell

### Domain specifikáció, fogalmak
Rendszeradminisztrátor: Az a személy aki a vicc adatbázis tartalmáért felelős.

Felhasználó: A végfelhasználó aki vicceket kér és értekeli őket.

Vicc: A vicc amit a felhasználók kérnek és értékelnek. Tartalmaz setup, punchline, kategória és értekelést.

Érékelés: Egy numerikus szám ami nagyobb minnél több pozitív értékelést kapott. Ez a szám mehet minuszba is ha több negatív értékelést kapott mint pozitívat.

Leaderboard: Az összes vicc és hozzátartozó értékelési szám.

### Absztrakt komponensek, ezek kapcsolatai
#### Felhasználói interakciók

A felhasználó az, aki a rendszer egyik fő komponense, és az alábbi interakciók révén éri el a kívánt szolgáltatásokat:
Viccek kérése:

A felhasználó kér egy viccet, ami a vicc generátort aktiválja. A vicc generátor visszaad egy viccet a rendszernek.

Viccek értékelése:

A felhasználó pontozza a viccet. Az értékelő rendszer tárolja és frissíti a vicc pontszámát.

Leaderboard megtekintése:

A felhasználó megtekintheti a leaderboardot, amely a legjobb viccek rangsorát mutatja. A leaderboard az összesített értékelések alapján frissül.

#### Háttérlogika


#### Adatbázis

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
