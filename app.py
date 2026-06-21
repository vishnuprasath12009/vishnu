from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>

<head>


    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Saira:wght@300;400;700&display=swap" rel="stylesheet">


<title>BIODATA OF S.VISHNU PRASATH</title>

<style>

body{
    margin:0;
    background:white;
    font-family: 'Saira', sans-serif;
    color:#222;
}

h1, h2, h3, p, button, a {
    font-family: inherit;
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
    font-size:55px;
    color:#0b3d91;
}


.card{
    background:##A9A9A9;
    padding:25px;
    margin:25px auto;
    border-radius:20px;
    max-width:800px;
    box-shadow:0 5px 20px #aaa;
}


.ber{
    background:#A9A9A9;
    padding:25px;
    margin:25px auto;
    border-radius:20px;
    max-width:800px;
    box-shadow:0 5px 20px #aaa;
}

h2 {
  font-size: 40px;
  color: #0b3d91;
  text-align: left;
}


.info{
    display:flex;
    justify-content:center;
    gap:30px;
    flex-wrap:wrap;
}

p {
    font-size: 25px;
    line-height: 1.7;
    color: #333;
    text-align: left;
}

.box{
    background:white;
    padding:20px;
    border-radius:15px;
    width:200px;
    box-shadow:0 3px 10px #bbb;
}


.army{
    background:#A9A9A9;
    color:black;
}

.army h2{
    color: black;
}


</style>

</head>


<body>


<div class="container">


<img class="profile"
src="/static/photo.jpg">


<h1>VISHNU PRASATH.S</h1>


<div class="card">


<h2>About Me</h2>


<p>                                                   
My name is S.Vishnu Prasath, and I hail from the vibrant city of Tirunelveli in Tamil Nadu. Born on September 12, 2009, I am currently a Class 12 student at Amrita Vidyalayam, Kanyakumari (Batch of 2026–2027)
</p>


</div>


<div class="card">


<h2>Family Background</h2>


<p>
I come from a supportive and hardworking family. My father, Mr. S. Selvan, is a dedicated businessman, and my mother, Mrs. S. Prabha, is the loving homemaker who keeps our lives beautifully organized.
</p>


</div>


<div class="card">


<h2>Early Life</h2>


<p>
I grew up in a scenic village called Madanpillai Tharmam. It is a place close to my heart, not just for its beauty, but because it is where I am surrounded by a wonderful network of relatives and six gem-like friends who have been a constant source of strength and happiness in my life.
</p>


</div>


<div class="card">


<h2>Hobbies</h2>


<p>
Outside of my studies, I am passionate about sports. My absolute favorite hobby is playing basketball, which keeps me active and teaches me the value of teamwork and discipline.
</p>

</div>


<div class="ber">


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


</div>



<div class="card army">


<h2>My Aim 🇮🇳</h2>

<p>
My ultimate goal is to serve the nation as an officer in the Indian Army. I ground my daily life in the core values of discipline, courage, and selfless service, aiming to lead by example and defend the country's sovereignty.
</p>

<button type="button" class="btn-show-more" onclick="window.open('https://www.instagram.com/_h4v0_x', '_blank')">click</button>

<a href="https://www.instagram.com/_h4v0_x" target="_blank" class="button-link instagram-btn">
        Follow me on Instagram
    </a>

</div>


</div>


</body>

</html>
"""


app.run(host="0.0.0.0", port=5000, debug=True)
