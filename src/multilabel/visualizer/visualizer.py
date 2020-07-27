import pandas
import webbrowser

STYLESHEET_NAME = 'mystyle'
HTML_FILENAME = 'output.html'


def create_html_template():
    return '''
        <html>
          <head><title>Results</title></head>
          <link rel="stylesheet" type="text/css" href="df_style.css"/>
          <body>
            {table}
          </body>
        </html>.
        '''


def display_dataframe(dataframe):
    pandas.set_option("colheader_justify", "center")   # FOR TABLE <th>

    html_string = create_html_template()

    # OUTPUT AN HTML FILE
    with open(HTML_FILENAME, 'w') as f:
        f.write(html_string.format(table=dataframe.to_html(classes=STYLESHEET_NAME)))

    webbrowser.open_new(HTML_FILENAME)