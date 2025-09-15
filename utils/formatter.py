from utils.process_utils import preprocess
def reformat_json(data):
    documents = [
        ' | '.join(f'{k}: {v if v.strip() != "" else "null"}' for k, v in item.items())
    for item in data
    ]
    return documents

def format_rag_results(results):
    if not results:
        return "Bu konuda yeterli bilgiye sahip değilim."
    
    formatted = []
    for r in results:  # sadece ilk 5 sonucu alalım
        bolum = r.get("Bölüm Adı", "Bilinmiyor")
        osym_kod = r.get("ÖSYM Program Kodu", "—")
        uni_turu = r.get("Üniversite Türü", "—")
        uni = r.get("Üniversite", "—")
        fakulte = r.get("Fakülte / Yüksekokul", "—")
        puan_turu = r.get("Puan Türü", "—")
        burs_turu = r.get("Burs Türü", "—")
        genel_kontenjan = r.get("Genel Kontenjan", "—")
        okul_birincisi = r.get("Okul Birincisi Kontenjanı", "—")
        toplam_kontenjan = r.get("Toplam Kontenjan", "—")
        genel_yerlesen = r.get("Genel Kontenjana Yerleşen", "—")
        okul_birincisi_yerlesen = r.get("Okul Birincisi Kontenjanına Yerleşen", "—")
        toplam_yerlesen = r.get("Toplam Yerleşen", "—")
        bos_kalan = r.get("Boş Kalan Kontenjan", "—")
        ilk_yerlesme_orani = r.get("İlk Yerleşme Oranı", "—")
        kayit_yaptirmayan = r.get("Yerleşip Kayıt Yaptırmayan", "—")
        ek_yerlesen = r.get("Ek Yerleşen", "—")
        son_puan_012 = r.get("0,12 Katsayı ile Yerleşen Son Kişinin Puanı", "—")
        son_sira_012 = r.get("0,12 Katsayı ile Yerleşen Son Kişinin Başarı Sırası", "—")
        tavan_puan = r.get("2024 Tavan Puan(0,12)", "—")
        tavan_sira = r.get("2024 Tavan Başarı Sırası(0,12)", "—")
        obp_2023 = r.get("2023'de Yerleşip 2024'de OBP'si Kırılarak Yerleşen Sayısı", "—")
        ort_obp = r.get("Yerleşenlerin Ortalama OBP'si", "—")
        ort_diploma = r.get("Yerleşenlerin Ortalama Diploma Notu", "—")
        
        formatted.append(
            f"- **{uni}** ({uni_turu}) - Bölüm: {bolum} Puan Türü[{puan_turu}]:\n"
            f"  Fakülte/Yüksekokul: {fakulte}\n"
            f"  Burs Türü: {burs_turu}\n"
            f"  Genel Kontenjan: {genel_kontenjan}, Okul Birincisi: {okul_birincisi}, Toplam Kontenjan: {toplam_kontenjan}\n"
            f"  Genel Yerleşen: {genel_yerlesen}, Okul Birincisi Yerleşen: {okul_birincisi_yerlesen}, Toplam Yerleşen: {toplam_yerlesen}\n"
            f"  Boş Kalan Kontenjan: {bos_kalan}, İlk Yerleşme Oranı: {ilk_yerlesme_orani}\n"
            f"  Yerleşip Kayıt Yaptırmayan: {kayit_yaptirmayan}, Ek Yerleşen: {ek_yerlesen}\n"
            f"  Son Puan 0,12: {son_puan_012}\n"
            f"  Son Başarı Sırası 0,12: {son_sira_012}\n"
            f"  2024 Tavan Puan: {tavan_puan}, 2024 Tavan Sıra: {tavan_sira}\n"
            f"  2023'de OBP kırılarak yerleşen: {obp_2023}\n"
            f"  Yerleşenlerin Ortalama OBP'si: {ort_obp}, Yerleşenlerin Ortalama Diploma Notu: {ort_diploma}"
        )
    return "\n\n".join(formatted)

def short_format(data):
    documents = []
    for r in data:
        bolum = r.get("Bölüm Adı", "Bilinmiyor")
        uni_turu = r.get("Üniversite Türü", "—")
        uni = r.get("Üniversite", "—")
        fakulte = r.get("Fakülte / Yüksekokul", "—")
        puan_turu = r.get("Puan Türü", "—")
        burs_turu = r.get("Burs Türü", "—")
        # kısa metin
        kisa_data = (
            f"Üniversite: {uni}, "
            f"Bölüm: {bolum}, "
            f"Üniversite Türü: {uni_turu}, "
            f"Fakülte: {fakulte}, "
            f"Puan Türü: {puan_turu}, "
            f"Burs Türü: {burs_turu}"
            )
        documents.append(preprocess(kisa_data))
    return documents