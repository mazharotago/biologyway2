from flask import Flask, render_template, request
import bioapps.nucleotide_counter as nc

app = Flask(__name__)

@ app.route('/')
def main():
    return (render_template("index.html"))

@ app.route('/bioinfo_tools')
def tools():
    return (render_template('app-page.html'))

@app.route('/about')
def about():
    return (render_template('about.html'))

#NucleotideCounterApp
@app.route('/nucleotidecount')
def nucleotide_counter():
    return render_template('nucleotide_counter_app.html')

@app.route('/nucleotidecount_app' , methods=['POST'])
def nucleotide_counter_app():
    nucleotide_seq = request.form['nucleotide_seq']
    dictionary,string_new = nc.nucleotide_counter(nucleotide_seq)

    return (render_template("nucleotide_counter_app_land.html", name=(dictionary,string_new)))











#WebSite_search_engine_maintainance
@app.route('/sitemap')
def sitemap():
    return render_template("sitemap.xml")



if __name__ == "__main__":
    app.run(debug=True)