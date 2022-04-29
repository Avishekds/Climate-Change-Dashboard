@@ -0,0 +1,11 @@
mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"avishek07.ds@gmail.com\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
