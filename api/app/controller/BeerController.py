from app import mysql

from flask import jsonify, render_template

class BeerController:
    def getBeers(self):
        try :
            cur = mysql.connection.cursor()
            cur.execute("SELECT nom_article, nom_marque, volume, titrage, prix_achat, nom_couleur, nom_type\
                        FROM article as a\
                        inner join marque as m using (id_marque)\
                        inner join couleur as c using (id_couleur)\
                        inner join type as t using (id_type)\
                ")
            resp = cur.fetchall()
            cur.close()
            beers = []
            if resp is not None:
                for beer in resp:
                    beers.append({
                        'nom_article': beer[0],
                        'nom_marque': beer[1],
                        'volume': int(beer[2]),
                        'titrage': float(beer[3]) if beer[3] else None,
                        'prix_ht': int(beer[4]),
                        'prix_15': int(beer[4])*1.15,
                        'couleur': beer[5],
                        'type': beer[6]
                    })
            return jsonify(beers)
        except Exception as e:
            print(e)
            return False

    def getCAByFabricant(self):
        try :
            cur = mysql.connection.cursor()
            cur.execute("select fab.NOM_FABRICANT, SUM(ROUND(a.Prix_achat*v.quantite,2)) CA FROM beer.ventes as v\
                        INNER JOIN beer.article a ON v.ID_ARTICLE=a.ID_ARTICLE\
                        INNER JOIN beer.marque f on a.ID_MARQUE=f.ID_MARQUE\
                        INNER JOIN beer.fabricant fab on f.ID_FABRICANT=fab.ID_FABRICANT\
                        group by fab.NOM_FABRICANT;\
                ")
            resp = cur.fetchall()
            cur.close()
            if resp is not None:
                beers = []
                for beer in resp:
                    beers.append({
                        'nom': beer[0],
                        'CA': round(float(beer[1])*1.15,2),
                    })
                return jsonify(beers)
            return jsonify({"message":"Nothing fetched"})
        except Exception as e:
            print(e)
            return False

    def getVariation(self):
        try :
            cur = mysql.connection.cursor()
            cur.execute("   select NOM_ARTICLE, qte15, qte16, ((qte16 - qte15) / qte15 * 100) as variation from article as a\
                            inner join (select id_article as id15, sum(quantite) as qte15 from ventes where annee = 2015 group by id_article) as r15\
                            inner join (select id_article as id16, sum(quantite) as qte16 from ventes where annee = 2016 group by id_article) as r16\
                            on  a.id_article = r15.id15 and r15.id15 = r16.id16 and a.id_article = r16.id16\
                            having variation between -1 and 1;")
            resp = cur.fetchall()
            cur.close()
            if resp is not None:
                beers = []
                for beer in resp:
                    beers.append({
                        'nom': beer[0],
                        'vente_2015': int(beer[1]),
                        'vente_2016': int(beer[2]),
                        'variation': float(beer[3]),
                    })
                return jsonify(beers)
            return False
        except Exception as e:
            print(e)
            return False


    def doc(self):
        return render_template("doc.html")
