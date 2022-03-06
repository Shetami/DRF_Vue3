<template>
<div class="filter-bar">
<nav>
         <label for="btn" class="button">Сортировать по
         <span class="fas fa-caret-down"></span>
         </label>
         <input type="checkbox" id="btn">
         <ul class="menu">
            <li><a href="#">Алфавиту</a></li>
            <li><a href="#">Рейтингу</a></li>
            <li><a href="#">Просмотрам</a></li>
            <li>
               <label for="btn-2" class="first">Дате
               <span class="fas fa-caret-down"></span>
               </label>
               <input type="checkbox" id="btn-2">
               <ul>
                  <li><a href="#">Новое</a></li>
                  <li><a href="#">Старое</a></li>
               </ul>
            </li>
         </ul>
</nav>
</div>
<div class="container-list">
  <div class="mangas">
      <div class="list-manga">
<div class="container_manga">
	<div class="block-manga">
	<div class="card-manga">
		<a href="#">
		<img class="img-manga-cart" src='../../public/1.png' alt="">
		</a>
	</div>
	<div class="title-manga">
	<a href="">
	<div class="card-title">Kimetsu no Yaba</div>
	</a>
	</div>
	</div>
</div>

</div>
  </div>
</div>
</template>

<script>


export default {
  name: "Home",
  data(){
    return {
      ContentList: []
    }
  },

}


</script>

<style scoped>
a{
	text-decoration: none;
}
.block-manga{
	width: 250px;
	height: 434px;
	display:inline-block
}
.card-manga{
	font-family: 'Cabin', sans-serif;
	background-color: #1f1c1c;
	width: 250px;
	height: 354px;
	border-top-left-radius: 10px;
	border-top-right-radius: 10px;
	border-bottom-right-radius:10px ;
	border-bottom-left-radius:10px ;
}
.img-manga-cart{
	width: 100%;
	border-top-left-radius: 10px;
	border-top-right-radius: 10px;
}
div div div div div{
  transition: transform 124ms linear;
	width: 100%;
	height: auto;
  display: block; /* Убираем полосу под картинкий */
}
div div div div:hover div{
  transform: scale(1.02);
}
.card-title{
	color: #fff;
	font-size: 20px;
	text-align: center;
	padding: 5px;
}
.title-manga{
	font-family: 'Cabin', sans-serif;
	background-color: #1f1c1c;
	width: 250px;
	height: 80px;
	border-bottom-right-radius:10px ;
	border-bottom-left-radius:10px ;
	display: flex;
  align-items: center;
  justify-content: center;
}
.container-manga{
	margin-top: 10px;
}
.list-manga{
	display: flex;
	flex-wrap: wrap;
	justify-content: space-around;
}

@import url('https://fonts.googleapis.com/css?family=Poppins:400,500,600,700&display=swap');

nav{
  position: relative;
  top: 20%;
  left: 300%;
  margin: 0 auto;
  background: #1b1b1b;
  width: 180px;
  min-height: 15px;
  display: table-cell;
  vertical-align: middle;
  padding: 10px 15px;
  border-radius: 5px;
}
.filter-bar{
  margin: 0 auto;
}
nav label{
  color: white;
  font-size: 14px;
  font-weight: 500;
  display: block;
  cursor: pointer;
}
.button span{
  padding: 4px 5px;
  float: right;
  min-height: 20px;
  transition: 0.5s;
}
.button span.rotate{
  transform: rotate(-180deg);
}
nav ul{
  position: absolute;
  background: #1b1b1b;
  list-style: none;
  left: 0;
  width: 100%;
  border-radius: 5px;
  display: none;
}
[id^=btn]:checked + ul{
  display: block;
}
nav .menu:before{
  position: absolute;
  content: '';
  height: 20px;
  width: 20px;
  background: #1b1b1b;
  right: 20px;
  top: -10px;
  transform: rotate(45deg);
  z-index: -1;
}
nav ul li{

  padding: 10px 15px;
  cursor: pointer;
  border-bottom: 1px solid rgba(0,0,0,0.2);
}
nav ul li label{
  font-size: 14px;
}
nav ul li a{
  color: white;
  text-decoration: none;
  font-size: 14px;
  display: block;
}
nav ul li a:hover,
nav ul li label:hover{
  color: cyan;
}
nav ul ul{
  position: static;
}
nav ul ul li{
  line-height: 30px;
  padding-left: 30px;
  border-bottom: none;
}
nav ul ul li a{
  color: #e6e6e6;
  font-size: 14px;
}
nav ul li span{
  padding: 4px 5px;
  float: right;
  min-height: 20px;
  transition: 0.5s;
}
nav ul li span.rotate{
  transform: rotate(-180deg);
}
input{
  display: none;
}
</style>