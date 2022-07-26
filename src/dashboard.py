from ctypes import util
from shutil import ReadError
import streamlit as st
# from streamlit_autorefresh import st_autorefresh
import pandas as pd
from random import random
import sys
import time

sys.path.append('./')

import utils
from wiki_consumer import WikiConsumer

class RealTimeDashboard:

    def __init__(self) -> None:
        self.c = WikiConsumer(utils.TOPIC_NAME)

    def run(self):
        
        st.set_page_config(
            page_title='Wikipedia real time',
            layout='wide'
        )

        
        st.title('Wikipedia Real Time dashboard')


        col = st.columns(6)
        col_row_2 = st.columns(6)

        col[0].write("Common Wikimedia:")
        col[1].write("Deutch Wikipedia:")
        col[2].write("English Wikipedia:")
        col[3].write("Eqiad Wikimedia")
        col[4].write("Persic Wikipedia")
        col[5].write("Wikidata") 

        col_row_2[0].write("Japanese Wikipedia")
        col_row_2[1].write("Georgian Wikipedia") 
        col_row_2[2].write("Russian Wikipedia") 
        col_row_2[3].write("Swedish Wikipedia") 
        col_row_2[4].write("Uzbekian Wikipedia") 
        col_row_2[5].write("Chinese Wikipedia") 


        common_kpi = col[0].empty()
        de_kpi = col[1].empty()
        en_kpi = col[2].empty()
        eqiad_kpi = col[3].empty()
        fa_kpi = col[4].empty()
        wikidata_kpi = col[5].empty()

        ja_kpi = col_row_2[0].empty()
        ge_kpi = col_row_2[1].empty()
        ru_kpi = col_row_2[2].empty()
        sv_kpi = col_row_2[3].empty()
        uz_kpi = col_row_2[4].empty()
        zh_kpi = col_row_2[5].empty()

        for x in self.c.run():
            if 'commons.wikimedia.org' in x.keys():
                with common_kpi:
                    st.metric("Artículos editados:", value=x['commons.wikimedia.org'])

            elif 'de.wikipedia.org' in x.keys(): 
                with de_kpi:
                    st.metric("Artículos editados:", value=x['de.wikipedia.org'])

            elif 'en.wikipedia.org' in x.keys(): 
                with en_kpi:
                    st.metric("Artículos editados:", value=x['en.wikipedia.org'])
            
            elif 'eqiad.mediawiki.recentchange' in x.keys(): 
                with eqiad_kpi:
                    st.metric("Artículos editados:", value=x['eqiad.mediawiki.recentchange'])

            elif 'www.wikidata.org' in x.keys(): 
                with wikidata_kpi:
                    st.metric("Artículos editados:", value=x['www.wikidata.org'])

            elif 'fa.wikipedia.org' in x.keys(): 
                with fa_kpi:
                    st.metric("Artículos editados:", value=x['fa.wikipedia.org'])            
            
            elif 'ka.wikipedia.org' in x.keys(): 
                with ge_kpi:
                    st.metric("Artículos editados:", value=x['ka.wikipedia.org'])

            elif 'ja.wikipedia.org' in x.keys(): 
                with ja_kpi:
                    st.metric("Artículos editados:", value=x['ja.wikipedia.org'])

            elif 'sv.wiktionary.org' in x.keys():
                with sv_kpi:
                    st.metric("Artículos editados:", value=x['sv.wiktionary.org'] )
            elif 'ru.wikipedia.org' in x.keys(): 
                with ru_kpi:
                    st.metric("Artículos editados:", value=x['ru.wikipedia.org'])

            elif 'uz.wikipedia.org' in x.keys(): 
                with uz_kpi:
                    st.metric("Artículos editados:", value=x['uz.wikipedia.org'])

            elif 'zh.wikipedia.org' in x.keys(): 
                with zh_kpi:
                    st.metric("Artículos editados:", value=x['zh.wikipedia.org'])
        
        # st_autorefresh(interval=1000, key="fizzbuzzcounter")



if __name__ == '__main__':

    rtd = RealTimeDashboard()
    rtd.run()