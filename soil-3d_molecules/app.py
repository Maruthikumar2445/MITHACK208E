from flask import Flask, render_template, request, redirect, url_for
from rdkit import Chem
from rdkit.Chem import AllChem
import require as py3Dmol

app = Flask(__name__)
def codon_category(codon):
     codon_dict={"UUU":"Phe","UUC":"Phe","UUA":"Leu","UUA":"Leu",
                 "UCU":"Ser","UCC":"Ser","UCA":"Ser","UCG":"Ser",
                 "UAU":"Tyr","UAC":"Tyr","UAA":"Stop","UAG":"Stop",
                 "UGU":"Cys","UGC":"Cys","UGA":"Stop","UGG":"Trp",
                 "CUU":"Leu","CUC":"Leu","CUA":"Leu","CUG":"Leu",
                 "CCU":"Pro","CAC":"Pro","CCA":"Pro","CCG":"Pro",
                 "CAU":"His","CAC":"His","CAA":"Gln","CAG":"Gln",
                 "CGU":"Arg","CGC":"Arg","CGA":"Arg","CGG":"Arg",
                 "AUU":"Ile","AUC":"Ile","AUA":"Ile","AUG":"Met",
                 "ACU":"Thr","ACC":"Thr","ACA":"Thr","ACG":"Thr",
                 "AAU":"Asn","AAC":"Asn","AAA":"Lys","AAG":"Lys",
                 "AGU":"Ser","AGC":"Ser","AGA":"Arg","AGG":"Arg",
                 "GUU":"Val","GUC":"Val","GUA":"Val","GUG":"Val",
                 "GCU":"Ala","GCC":"Ala","GCA":"Ala","GCA":"Ala",
                 "GAU":"Asp","GAC":"Asp","GAA":"Glu","GAG":"Glu",
                 "GGU":"Gly","GGC":"Gly","GGA":"Gly","GGG":"Gly"}
     return codon_dict[codon]
def amino_acid(sequence):
     sequence_length=len(sequence)-3
     amino=""
     for i in range(0,sequence_length,3):
         code=str(sequence[i]+sequence[i+1]+sequence[i+2])
         amino+=codon_category(code)
         amino+='-'
     return amino[:-1]
def Smile_String(smile):
     Smile_dict={"Ala":"CC(C(=O)O)N","Cys":" CSCC(C(=O)O)N","Asp":"CC(C(=O)O)C(=O)O",
                 "Glu":"CC(C(=O)O)C(=O)OC(C)C","Phe":"Nc1ccccc1C(=O)O",
                 "Gly":"NCC(=O)O","His":"Nc1c[nH]cn1C(=O)O","Ile":"CCC(C)C(C(=O)O)N",
                 "Lys":"NCCCCC@HN","Leu":"CCC(C)CC(C(=O)O)N","Met":"CSCCC(C(=O)O)N",
                 "Asn":"CC(C(=O)O)C(=O)N","Pro":"CC1CC(C(=O)N)C1","Gln":"CC(C(=O)O)C(=O)NC",
                 "Arg":"N=C(N)NCCCCC@HN","Ser":"OCC(C(=O)O)N","Thr":"CC(C(=O)O)C(O)N",
                 "Val":"CCC(C)C(C(=O)O)N","Trp":"Nc1ccc2c(c1)CC@@HN2","Tyr":"Nc1ccc(O)cc1C(=O)O"}
     return Smile_dict[smile]
 
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        smiles = request.form['smiles']
        dump_smile = smiles
        k=amino_acid(smiles)
        S=k.split('-')
        print(S)
        smiles = ""
        for i in S:
            smiles+=Smile_String(i)
        print(smiles)
        mol = Chem.MolFromSmiles(smiles)

        if mol is not None:
            
            AllChem.EmbedMolecule(mol, randomSeed=42)

            viewer = py3Dmol.view(width=500, height=500)
            viewer.addModel(Chem.MolToMolBlock(mol), "mol")
            viewer.setStyle({"stick": {}})
            viewer.zoomTo()

            mol3d_html = viewer.render()
            html_main= viewer._make_html()
            html = f'''
            <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>3D Protein Visualization</title>
    <!-- Link to Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body style="
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1a2a6c, #b21f1f, #fdbb2d);
            color: var(--text-light);
            min-height: 100vh;
            overflow-x: hidden;"
        >

    <!-- Navigation bar using Bootstrap -->
    

    <!-- Hero section using Bootstrap -->
    <section class="hero text-center" style="background-image: url('background-image.jpg'); background-size: cover; background-position: center; padding: 100px 0; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);">
        <div class="container">
        <h1 style=" 
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 1rem;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
            animation: fadeInUp 1s ease;
            color:white;
        ">Kalasalingam Academy of Research and Education</h1>
         <h2 style=" 
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 1rem;
            color:white;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
            animation: fadeInUp 1s ease;
        ">Soil Based Chemical Testing Through GIS</h2>
        
        </div>
        <h1 style=" 
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 1rem;
            color:white;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
            animation: fadeInUp 1s ease;
        "">3D visualization of {dump_smile}</h1>
    </section>
    <section id="3dview" style="display: flex; justify-content: center; align-items: center; height: 60vh;">
        {html_main}
    </section>

    <footer class="bg-light py-4" style="background-color: transparent !important; color: #fff; padding: 10px 0;">
        <div class="container text-center">
            <div class="footer-logo" style="font-size: 18px;">
                <p style="padding:5px;">Developed By <b> Team ARANYA JAL</b></p>
            </div>
           
        </div>
    </footer>

    <!-- Link to Bootstrap JavaScript Scripts -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.3/dist/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>
'''         
            return html
        else:
            error_message = "Invalid SMILES input. Please try again."
            return render_template('index.html', error_message=error_message)

    return render_template('index.html')

@app.route('/output')
def output():
    smiles = request.args.get('smiles')
    mol3d_html = request.args.get('mol3d_html')
    return render_template("main.html")

if __name__ == '__main__':
    app.run(debug=True)