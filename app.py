from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>

<head>

<title>Biodata of Vishnu Prasath</title>

<style>

body{
    margin:0;
    background:white;
    font-family:Arial, sans-serif;
    color:#222;
}


.container{
    width:80%;
    margin:auto;
    padding:40px;
    text-align:center;
    animation:fade 2s;
}


@keyframes fade{
    from{
        opacity:0;
        transform:translateY(30px);
    }
    to{
        opacity:1;
        transform:translateY(0);
    }
}


.profile{
    width:180px;
    height:180px;
    border-radius:50%;
    object-fit:cover;
    border:5px solid #111;
    animation:float 3s infinite;
}


@keyframes float{
    50%{
        transform:translateY(-15px);
    }
}


h1{
    font-size:45px;
    color:#0b3d91;
}


.card{
    background:#f5f5f5;
    padding:25px;
    margin:25px auto;
    border-radius:20px;
    max-width:800px;
    box-shadow:0 5px 20px #aaa;
}


h2{
    color:#0b3d91;
}


.info{
    display:flex;
    justify-content:center;
    gap:30px;
    flex-wrap:wrap;
}


.box{
    background:white;
    padding:20px;
    border-radius:15px;
    width:200px;
    box-shadow:0 3px 10px #bbb;
}


.army{
    background:#111;
    color:white;
}


</style>

</head>


<body>


<div class="container">


<img class="profile"
src="/static/photo.jpg">


<h1>BIODATA OF VISHNU PRASATH</h1>


<div class="card">


<h2>About Me</h2>


<p>                                                   
My name is S. Vishnu Prasath, and I hail from the vibrant city of Tirunelveli in Tamil Nadu. Born on September 12, 2009, I am currently a Class 12 student at Amrita Vidyalayam, Kanyakumari (Batch of 2026–2027)
</p>


<p>
I come from a supportive and hardworking family. My father, Mr. S. Selvan, is a dedicated businessman, and my mother, Mrs. S. Prabha, is the loving homemaker who keeps our lives beautifully organized.
</p>

<p>
I grew up in a scenic village called Madanpillai Tharmam. It is a place close to my heart, not just for its beauty, but because it is where I am surrounded by a wonderful network of relatives and six gem-like friends who have been a constant source of strength and happiness in my life.
</p>

<p>
Outside of my studies, I am passionate about sports. My absolute favorite hobby is playing basketball, which keeps me active and teaches me the value of teamwork and discipline.
</p>

</div>



<div class="info">


<div class="box">
<h3>Class</h3>
<p>12th</p>
</div>


<div class="box">
<h3>Height</h3>
<p>190+ cm</p>
</div>


<div class="box">
<h3>Weight</h3>
<p>70 kg</p>
</div>


</div>



<div class="card army">


<h2>My Aim 🇮🇳</h2>

<p>
AIM is to become an Indian Army officer.
I believe in discipline, courage, dedication and service to the country.
</p>


</div>


</div>


</body>

</html>
"""


app.run(host="0.0.0.0", port=5000, debug=True)
