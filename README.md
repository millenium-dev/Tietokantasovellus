
07.03.2021
--------------------

# Heroku

Heroku osoite: https://pankkisovellus1.herokuapp.com/

Sain refspec ongelman selvitettyä ja vihdoinkin ladattua sovelluksen herokuun

# Millainen sovellus on?
Sovellus on helppokäyttöinen ja selkeä pankkisovellus. Sovelluksesta löytyy joitain keskeisiä pankkitoimintoja sekä paljon muuta tietoa liittyen Attica Pankkiin (sovelluksessa oleva kuvitteellinen pankki) ja sen toimiympäristöön. Sovellus on ulkoisesti mielestäni hauska ja ainakin erilainen - sen teema ja tunnelma on selvästi japanilainen samalla kun sen visuaalinen ilme pysyy joksenkin yhtenäisenä läpi koko sovelluksen.

# Miten sovellusta voi testata?
Sovellusta voi testata luomalla käyttäjätilin. Tietyt sivut ovat toki myös nähtävissä ilman kirjautumista. Sovellusta voi testata erilaisia esim tietoa ja infoa sisältävien sivujen avaamisen lisäksi muun muassa luomalla käyttäjätilin luomisen jälkeen pankkitilin jolle voi yrittää suorittaa erilaisia pankkitoimintoja. Näitä ovat muun muassa rahan nosto, talletus sekä tilisiirto. Näitä toimintoja voi kokeilla osiosta "Pankkipalvelut". Tämän lisäksi osiossa "Pankkipalvelut" voi tarkastella myös aikaisempia talletuksia, tilin saldo sekä omaa tilihistoriaansa. Sovellusta voi myös kokeilla syöttämällä sille arvoja jotka ovat vastoin annettuja ohjeita tai kokeilemalla siirtää esim negatiivisen summan toisen käyttäjän tilille.

# Plussat
- Sovelluksen käyttöliittymä on suhteellisen helppokäyttöinen
- Sovellus on visuaalisesti pääosin miellyttävä, joskin kaukana ammattilaisen tekemästä
- Sovellus toimii/on toiminut halutulla tavalla eikä mitään suurempaa 
- Sovelluksen toiminnot ovat selkeitä ja väärästä tiedosta on pyritty ilmoittamaan 
- Koodin tyyli (sovelluksen CSS-ulkoasu) on suhteellisen yhdenmukainen ja muuttujat ja funktiot on nimetty kuvaavalla tavalla
- Tietokannat on mielestäni suunniteltu kohtalaisesti, turhaa tietoa ei haeta sekä taulut ja sarakkeet on pääosin nimetty kuvaavalla tavalla
- Tietoturvan osalta SQL-injektiot ja XSS-haavoittuvuudet on toivottavasti onnistuttu välttämään

# Miinukset
- Sovellus voisi olla joiltain osin monipuolisempi ja siinä olisi voitu hyödyntää enemmän "alerteja" ja Python- ja JavaScript koodia.
- Tilin luonti ja tarkemmin ottaen tilinumeron anto on nyt hoidettu tavalla joka ei ole pidemmän päälle toimiva
- Olisin voinut hoitaa CSS-koodin jotenkin järkevämmin, nyt sama kohtalaisen pitkä pätkä löytyy useammasta HTML-tiedostosta
- Joskus on käytetty liiankin montaa kyselyä tietokannoista tietoa haettaessa
- Sovelluksen tietoturvassa on vielä parantamisen varaa, esim env-tiedosto jäi poistamatta sekä Palaute osion syöte tarkistamatta
- Projekti kulki omalta osalta kohtalaisesti mutta olisi ollut huomattavasti parempi mikäli olisin saanut sovelluksen aikaisemmin Herokuun ja ollut tämän osalta vielä yritteliäämpi, parannettavaa siis jäi

# Muuta
- Sovelluksen kehittäminen oli suurimmalta osin erittäin mielekästä puuha
- Koen että sain tästä sekä paljon lisää osaamista sekä kipinän oppia lisää sovelluskehitykestä ja UX-suunnittelusta


- - - - - - - - - - - - - - - - - - --  - - --  - - - --  - - - - -- - - - - - - - - - - - --- -- - - - 

01.02.2021
------------------------

# Tietokantasovellus - Pankkitili

Tässä README tiedostossa esittelen suunnitelmani tietokantasovellusprojektia varten. 

# Sovelluksen idea

Ideanani on rakentaa sovellus joka toimii pankkitilinä. 

# Sovelluksen tarkoitus

Sovelluksen on tarkoitus toimia alustana jossa käyttäjä voi avata kuvitellun pankkitilin, siirtää rahaa toiselle tilille sekä tarkastaa tilinsä saldon. 

# Sovelluksen toiminta

Sovelluksen toiminta perustuu Python Flaskiin ja SQL tietokantaan. Python Flaskin avulla sovellus toteuttaa sovelluksen jonka toiminta perustuu toisaalta siihen että käyttäjän tiedot, pankkitilin saldo, talletetukset sekä nostot ja tehdyt siirrot tallentaan tietokantaan. 

# Sovelluksen lisätoiminnot

Sovellukseen liittyen minulla on joitain ideoita sen suhteen minkälaisia lisätoimintoja sovellus voisi tarjota. Yksi idea on se että sovellus näyttäisi kaikki transaktiot jotka käyttäjä on aikaisemmin tehnyt sekä erottelisi ne maksettuihin ja saatuihin. Toinen lisätoiminto olisi taas se että asiakas voi poistaa tilinsä. 

# Muut olennaiset asiat

Tämän lisäksi haluan kiinnittää huomiota erityisesti sovelluksen tietoturvaan.

---------------------------------------------------------------------------------------------------------------
07.02.2021

# Sovelluksen nykytilanne

Sovelluksella on joksenkin toimiva pohja joskin siitä puuttuu vielä lähes kaikki tietokantoihin liittyvä joiden lisääminen onkin seuraava fokukseni aihe.

# Toteutettavien asioiden lista (päivittyvä)

0.1. Saada sovellus toimimaan Herokun kanssa
0.2. Muokata login ja register sivuista sovelluksen näköiset

1.	Add functionality for money deposits and show account balance
2.	Add functionality for withdrawing money!
3.	Add functionality for transferring money!
4.	Add functionality for showing all transmissions

Lista jatkuu sitä mukaa kun edelliset kohdat valmistuvat.

# Plussat

- Olen joksenkin tyytyväinen sovelluksen visuaaliseen ilmeeseen, vaikka se onkin vielä todella kaukana todellisten huippusivujen ilmeestä.
- Koen oppineeni paljon uutta niin css:ästä kuin html:ästä.
- Koen että minulla on aika selvä visio sen suhteen miten vien sovellusta eteenpäin. 
- Sovelluksen tekeminen on ollut hauskaa. 

# Miinukset

- En ole saanut Herokua toimimaan - refspec ongelma. 
- Sovellus on edistynyt mutta varsinaisia tietokantaan liittyviä toimintoja en ole vielä siihen juurikaan sisällyttänyt.
- Sovelluksessa on vielä paljon esimerkkisovellukseen liittyviä asioita joita harvennan sitä mukaa kun sovellus edistyy.

# Kysymykset

Hyviä lähteitä vaativamman CSS:n opetteluun?

# Muuta

Kiitos ensimmäisen välipalutuksen palauttessta.
