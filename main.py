<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Bharath Industrial | Welding & Industrial Works</title>

<style>

body{
font-family: Arial;
margin:0;
background:#f0f2f5;
}

/* Header */

header{
background:#1877f2;
color:white;
padding:15px;
font-size:24px;
font-weight:bold;
display:flex;
justify-content:space-between;
align-items:center;
}

.contact{
font-size:16px;
}

/* Layout */

.container{
display:flex;
}

/* Sidebar */

.sidebar{
width:220px;
background:white;
padding:20px;
height:100vh;
box-shadow:0 0 5px rgba(0,0,0,0.1);
}

.sidebar a{
display:block;
padding:10px;
text-decoration:none;
color:black;
margin-bottom:5px;
border-radius:5px;
}

.sidebar a:hover{
background:#f0f2f5;
}

/* Content */

.content{
flex:1;
padding:20px;
}

/* Card */

.card{
background:white;
padding:20px;
margin-bottom:20px;
border-radius:10px;
box-shadow:0 0 5px rgba(0,0,0,0.1);
}

/* Image */

.card img{
width:100%;
border-radius:10px;
margin-top:10px;
}

/* Price table */

table{
width:100%;
border-collapse:collapse;
margin-top:10px;
}

table, th, td{
border:1px solid #ddd;
}

th,td{
padding:10px;
text-align:left;
}

/* Comment section */

.comment-box{
margin-top:10px;
}

.comment-box input{
width:80%;
padding:8px;
}

.comment-box button{
padding:8px 15px;
background:#1877f2;
color:white;
border:none;
}

.comments{
margin-top:10px;
font-size:14px;
}

.job{
background:#fff3cd;
padding:10px;
margin-top:10px;
border-radius:5px;
}

</style>
</head>

<body>

<header>
Bharath Industrial
<div class="contact">📞 7902984770</div>
</header>

<div class="container">

<!-- Sidebar -->

<div class="sidebar">

<a href="#">Home</a>
<a href="#">Price List</a>
<a href="#">Hen Cage Welding</a>
<a href="#">Welder Vacancy</a>
<a href="#">Contact</a>

</div>


<!-- Main Content -->

<div class="content">

<!-- Industry Photo -->

<div class="card">

<h2>Bharath Industrial Welding Works</h2>

<p>Professional industrial welding, contract works, sheet installation and site works.</p>

<img src="https://images.unsplash.com/photo-1581092580497-e0d23cbdf1dc" alt="Welding Industry">

<div class="comment-box">
<input type="text" placeholder="Write a comment...">
<button onclick="addComment(this)">Post</button>
</div>

<div class="comments"></div>

</div>


<!-- Price List -->

<div class="card">

<h2>Industrial Work Price List</h2>

<table>

<tr>
<th>Work Type</th>
<th>Price</th>
</tr>

<tr>
<td>Contract Welding Work</td>
<td>₹1500 / Day</td>
</tr>

<tr>
<td>Sheet Installation</td>
<td>₹120 / sq.ft</td>
</tr>

<tr>
<td>Industrial Fabrication</td>
<td>₹2000 / Project</td>
</tr>

<tr>
<td>Site Welding Works</td>
<td>₹1800 / Day</td>
</tr>

<tr>
<td>Station Welding Works</td>
<td>₹1600 / Day</td>
</tr>

</table>

</div>


<!-- Hen Cage Welding -->

<div class="card">

<h2>Hen Cage Welding Works</h2>

<p>We manufacture strong and durable poultry cages for farms and commercial poultry businesses.</p>

<img src="https://images.unsplash.com/photo-1598514982849-6e23b8c2a52b" alt="Hen Cage Welding">

<ul>
<li>Heavy duty iron cages</li>
<li>Long life welding</li>
<li>Custom sizes available</li>
<li>Farm installation support</li>
</ul>

</div>


<!-- Welder Vacancy -->

<div class="card">

<h2>Welder Job Vacancy</h2>

<div class="job">

<p><b>Position:</b> Industrial Welder</p>
<p><b>Experience:</b> 1-3 Years</p>
<p><b>Location:</b> Site / Workshop</p>
<p><b>Salary:</b> Negotiable</p>

<p>Interested candidates contact:</p>

<h3>📞 7902984770</h3>

</div>

</div>


<!-- Contact -->

<div class="card">

<h2>Contact Bharath Industrial</h2>

<p>For welding works, industrial fabrication and poultry cage welding.</p>

<p><b>Phone:</b> 7902984770</p>

</div>

</div>

</div>


<script>

function addComment(btn){

let input = btn.previousElementSibling;
let text = input.value;

if(text=="") return;

let comments = btn.parentElement.nextElementSibling;

let p = document.createElement("p");
p.textContent = "💬 " + text;

comments.appendChild(p);

input.value="";

}

</script>

</body>
</html>
