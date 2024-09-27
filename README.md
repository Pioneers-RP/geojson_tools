# geojson_tools
3 python files to serve as tools to handle our cool geojson files

# Main goal :
2 files are actually used as scripts. 
    - 1: geojson_interpret, allows you to format a prompt. You simply need to invoke it this way : "python geojson_interpret.py ``filename``". It will format a ChatGPT-4o prompt
    - 2: geojson_writer, allows you to send back the datas in the geojson file. For this, you need to edit ``geojson_dict.py`` putting in the ``geojson_dict`` variable the ChatGPT-4's answer, and the filename with the actual filename. Then, you only have to do ``python geojson_writer.py`.
My recommandations are using command lines, but I may create a TKinter app to allow easy and accessible modifications !