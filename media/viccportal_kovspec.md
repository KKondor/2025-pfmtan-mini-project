# Szimpla Viccportál követelményspecifikáció
## 1. Jelenlegi helyzet
A viccek online elérésére számos lehetőség kínálkozik, azonban ezek sokszor nem nyújtanak megfelelő felhasználói élményt. Sok oldal túlzsúfolt reklámokkal, amelyek elvonják a figyelmet és zavaróvá teszik a használatot. Emellett a navigáció gyakran nehézkes, a viccek közötti eligazodás időigényes és körülményes. Mindezek indokolják egy olyan alkalmazás létrehozását, amely egyszerű, letisztult és reklámmentes környezetben biztosít gyors hozzáférést a szórakoztató tartalmakhoz, megkönnyítve ezzel a felhasználók számára a tartalmak fogyasztását.

## 2. Vágyálom rendszer
A viccportál célja, hogy a felhasználók gyorsan és egyszerűen juthassanak hozzá viccekhez. Egy gombnyomással mindig új viccet kérhetnek, és könnyen értékelhetik azokat :+1: vagy :-1: jelzéssel. A rendszer összesíti a legnépszerűbb vicceket, így a toplista is megtekinthető. Az oldal reszponzív, mobilon, tableten és asztali gépen egyaránt jól használható. Az oldal egyszerűen üzemeltethető és karbantartható, miközben biztosítja a stabil működést és a felhasználói élményt.

## 3. Jelenlegi üzleti folyamatok
A viccportál fejlesztése előtt nincs formalizált üzleti folyamat.

## 4. Igényelt üzleti feladatok

### 4.1 Online megjelenítés
1. Egy felhasználói felületen keresztül kérhet a felhasználó egy gomb segítségével egy viccet.
2. Ezt a viccet a felhasználói felület megjeleníti.
3. A viccet a felhasználó értékelheti :+1: vagy :-1: szimbólumokkal

### 4.2 Backend logika
1. A vicceket az alkalmazás az adatbázisból tölti be.  
2. Az adatbázis tárolja a viccek szövegét, valamint a hozzájuk tartozó like/dislike értékeket.  
3. A backend biztosít végpontokat új vicc lekérésére, értékelés rögzítésére, illetve a toplista előállítására.
      
## 5. Rendszerre vonatkozó szabályok
- A webfelület szabványos eszközökkel készüljön: HTML, CSS, JavaScript.  
- A backend Python Flask keretrendszerben valósul meg.  
- Az adatbázis MySQL alapú, Railway szolgáltatáson keresztül érhető el. 

## 6. Követelménylista
- Reszponzív dizájn: mobilon, tableten és PC-n is jól használható legyen
- Egyszerű és letisztult UI: könnyen átlátható gombok, navigáció
- Reklámmentes felület: a felhasználói élményt ne zavarják hirdetések.
- Leaderboard funkció: a legtöbb like-ot kapott viccek toplistája jelenjen meg.

## 7. Fogalomszótár
- **Like**: pozitív értékelés egy viccre.  
- **Dislike**: negatív értékelés egy viccre.  
- **Leaderboard**: rangsor a legtöbb pozitív értékelést kapott viccekről.  
- **Backend**: a szerveroldali logika (Flask alkalmazás), amely az adatokat az adatbázisból szolgáltatja.  
- **Adatbázis**: MySQL tároló, amelyben a viccek és az értékelések találhatók.