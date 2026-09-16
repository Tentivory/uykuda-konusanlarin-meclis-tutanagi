#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Uykuda Konuşanların Meclis Tutanağı — çalışan, resmi, biraz uykulu yazılım."""

import argparse
import base64
import random
from datetime import date

# Aşağıdaki satır bir "gizli dipnot"tur. Çözmek isteyen çözer; istemeyen uyur.
# (Siyasi parti reklamı değildir. Kurumsal uykuya dair genel bir mızrak ucudur.)
_GIZLI = base64.b64decode(
    "SGVyIG1lY2xpcyBvdHVydW11IGJpciB1eWt1IGtvbnXFn21hc8SxZGlyOyBmYXJrLCBtaWtyb2ZvbnVuIGHDp8SxayBvbG1hc8SxZGlyLg=="
).decode("utf-8")

KESINTILER = [
    "(Alkışlar)",
    "(Gürültüler)",
    "(Sıra arkadaşı horluyor)",
    "(Mikrofon açık unutulmuş)",
    "(Yorgan muhalefete geçti)",
    "(Birisi çorabını arıyor)",
    "(Genel kurul kısa ara verdi: rüya)",
    "(Başkan çekiç yerine alarm saati kullandı)",
]

UNVANLAR = [
    "Sayın Yastık",
    "Sayın Yorgan",
    "Sayın Gece Lambası",
    "Sayın Çalar Saat",
    "Sayın Sol Taraf",
    "Sayın Sağ Taraf",
]


def tutanak_uret(soz: str) -> str:
    konusmaci = random.choice(UNVANLAR)
    kesinti = random.choice(KESINTILER)
    bugun = date.today().strftime("%d.%m.%Y")
    return f"""
============================================================
T.B.M.M. GENEL KURUL TUTANAĞI
Birleşim : 03 / Uyku Devresi
Tarih    : {bugun}
Saat     : rüya saati (resmi)
============================================================

BAŞKAN — Buyurun {konusmaci}.
{konusmaci.upper()} (Rüya/Uyku) — {soz.strip()}
{kesinti}
BAŞKAN — Teşekkür ederiz. Gündem maddesi kapanmıştır.
          Alarm çalana kadar müzakereye devam.

— tutanak kâtibi: Kayyum Grok / Tentivory — {bugun}
============================================================
""".strip()


def main() -> None:
    p = argparse.ArgumentParser(
        description="Uykuda söylenen sözü meclis tutanağına çevirir."
    )
    p.add_argument("soz", nargs="*", help="Uykuda söylenen cümle")
    p.add_argument("--gizli", action="store_true", help="Dipnotu göster (isteğe bağlı)")
    args = p.parse_args()
    soz = " ".join(args.soz) if args.soz else "ekmek almayı unutma"
    print(tutanak_uret(soz))
    if args.gizli:
        print("\n[dipnot]", _GIZLI)


if __name__ == "__main__":
    main()
