from flask import Flask, render_template, request
import bioapps.nucleotide_counter as nc
import bioapps.dna_to_rna_converter as drconv
import bioapps.gc_content_calc as gc_calc

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
@app.route('/tool/nucleotidecount')
def nucleotide_counter():
    return render_template('nucleotide_counter_app.html')

@app.route('/tool/nucleotidecount' , methods=['POST'])
def nucleotide_counter_app():
    nucleotide_seq = request.form['nucleotide_seq']
    dictionary,string_new = nc.nucleotide_counter(nucleotide_seq)
    return (render_template("nucleotide_counter_app_land.html", name=(dictionary, string_new)))

#DNA-to-RNA converter App
@app.route('/tool/dnatornaconvert')
def dna_to_rna_conv():
    return (render_template('dna_to_rna_converter_app.html'))

@app.route('/tool/dnatornaconvert', methods=['POST'])
def dna_to_rna_conv_land():
    d_t_r_sequence = request.form['nucleotide_seq']
    rna_seq = drconv.dna_to_rna_convert(d_t_r_sequence)
    return (render_template('dna_to_rna_converter_app_land.html', dtr_seq=rna_seq))

#GC-content-estimator

@app.route('/tool/gccontent')
def gc_content():
    return (render_template('gc_content_app.html'))

@app.route('/tool/gccontent', methods=['POST'])
def gc_content_land():
    gc_content_count = request.form['nucleotide_seq']
    data = gc_calc.data_org(gc_content_count)
    if data == "Multiple sequences are having same name - change name":
        return (render_template('gc_content_app_land.html', gc_content_count=data, sequence=gc_content_count))
    elif data == "function breaks":
        return (render_template('gc_content_app_land.html', gc_content_count=data, sequence=gc_content_count))
    else:

        output = gc_calc.evaluation(data)
        if output == "bad sequence":
            return (render_template('gc_content_app_land.html', gc_content_count=output, sequence=gc_content_count))
        else:
            values_gc_content = gc_calc.gc_content(output)
            return (render_template('gc_content_app_land.html', gc_content_count=values_gc_content, sequence=gc_content_count))













#WebSite_search_engine_maintainance
@app.route('/sitemap')
def sitemap():
    return render_template("sitemap.xml")



if __name__ == "__main__":
    app.run(debug=True)