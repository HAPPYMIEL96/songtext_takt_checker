{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fnil\fcharset0 AppleColorEmoji;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import re\
import streamlit as st\
\
st.title("
\f1 \uc0\u55357 \u56541 
\f0  Songtext Takt-Checker")\
\
st.markdown("Gib hier deinen Songtext Zeile f\'fcr Zeile ein. Das Tool pr\'fcft, ob jede Zeile im Takt liegt (ca. 10\'9612 Silben f\'fcr 4/4-Takt).")\
\
song_input = st.text_area("
\f1 \uc0\u55356 \u57252 
\f0  Dein Songtext (jede Zeile einzeln)", height=200)\
\
\
def count_syllables(line):\
    # Sehr einfache Silbenz\'e4hlung auf Basis von Vokalen\
    return len(re.findall(r'[aeiouy\'e4\'f6\'fcAEIOUY\'c4\'d6\'dc]+', line))\
\
def check_lines_for_rhythm(song_lines):\
    feedback = []\
    for i, line in enumerate(song_lines, start=1):\
        syllables = count_syllables(line)\
        if 9 <= syllables <= 13:\
            comment = "
\f1 \uc0\u9989 
\f0  Gut im Takt (ca. 10\'9612 Silben)"\
        elif syllables < 9:\
            comment = "
\f1 \uc0\u9888 \u65039 
\f0  Eher zu kurz \'96 evtl. erweitern?"\
        else:\
            comment = "
\f1 \uc0\u9888 \u65039 
\f0  Eher zu lang \'96 evtl. k\'fcrzen?"\
        feedback.append(f"**Zeile \{i\}:** \{syllables\} Silben \'96 \{comment\}\\n> \{line\}")\
    return feedback\
\
if song_input:\
    lines = [line.strip() for line in song_input.strip().split("\\n") if line.strip()]\
    result = check_lines_for_rhythm(lines)\
\
    st.markdown("---")\
    st.subheader("
\f1 \uc0\u55358 \u56800 
\f0  Analyse-Ergebnis")\
    for entry in result:\
        st.markdown(entry)\
}