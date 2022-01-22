// le dom une arborescence qui est utiliser pour gérer l'interface visuelle du site
//banniere
var i = 0;
var images = [];
var temps =2000;
var nombreImages = 8;
var Banniere =  $('.Banniere'); //  est du Jquery
var Boutons =  $('.BoutonContainer');

var BoutonGauche =  $('.Gauche');
var BoutonDroite =  $('.Droite');
var BoutonPlayPause =  $('#PlayPause');
var Play="https://img.icons8.com/metro/1600/play.png";
var Pause="https://img.icons8.com/metro/1600/pause.png";
var Timer;

const body = document.body
const div = document.createElement("div")

const strong = document.createElement("strong")
strong.innerText = "bob"
div.append(strong)
div.setAttribute("id", "dom")
const dom = document.getElementById('Dom')
dom.append(div)


//change Images
function ChangeImage(){
//alert(images[i]);
  document.ImageBanniere.src = images[i]
//    document.ImageBanniere.src = images[i].substring(11,25);


//    alert(images.length)
  if(i < nombreImages ){
    i++;
  }else{
    i=0;
  }
    //alert(i);
   Timer = setTimeout("ChangeImage()", temps);
}
window.onload = ChangeImage;


//liste images
//images[0] = "{% static 'images/koe.jpg' %}";
//images[1] = "{% static 'images/koe.jpg' %}";
//images[2] = "{% static 'images/Bmw.jpg' %}";
//images[3] = "{% static 'images/koe.jpg' %}";
//images[4] = "{% static 'images/koe.jpg' %}";
//images[5] = "{% static 'images/Bmw.jpg' %}";
//images[6] = "{% static 'images/koe.jpg' %}";
//images[7] = "{% static 'images/koe.jpg' %}";
//images[8] = "{% static 'images/Bmw.jpg' %}";
images[0] = 'images/koe.jpg';
images[1] = 'images/koe.jpg';
images[2] = 'images/Bmw.jpg';
images[3] = 'images/koe.jpg';
images[4] = 'images/koe.jpg';
images[5] = 'images/Bmw.jpg';
images[6] = 'images/koe.jpg';
images[7] = 'images/koe.jpg';
images[8] = 'images/Bmw.jpg';

//Bouton onhover onout
Banniere.mouseover(AfficheBouton); //  mouseover est un event qui appelle une fonction qui utilise le callback
Banniere.mouseleave(CacheBouton);  //  fonction qui utilise le callback
// un callback c'est appeler une fonction en mettant une fonction dans le paramètre

function AfficheBouton() { // agis sur le dom
  Boutons.css('visibility','visible')
}
function CacheBouton() { // agis sur le dom
   Boutons.css('visibility','hidden')
}

//bouton clique est aussi un event
BoutonGauche.click(ImagePrecedente); //
BoutonDroite.click(ImageSuivante);
BoutonPlayPause.click(PlayPause);

function ImagePrecedente() {
  document.PlayPause.src=Play;
clearTimeout(Timer);
   if( i===0){
      document.ImageBanniere.src = images[7];
      i=8;
  }
  else if( i===1){
      document.ImageBanniere.src = images[0];
        i=1;
  }
  else{
      document.ImageBanniere.src = images[i-1];
        i=i-1;
  }
}


function ImageSuivante() {
  document.PlayPause.src=Play;
clearTimeout(Timer);
 if( i===0){
      document.ImageBanniere.src = images[8];
      i=0;
  }
  else if( i===8){
      document.ImageBanniere.src = images[8];
        i=0;
  }
  else{
      document.ImageBanniere.src = images[i];
    i=i+1;

  }
}

// play pause
function PlayPause() {
if( document.PlayPause.src===Pause){
  document.PlayPause.src=Play;
clearTimeout(Timer);
}else{
  document.PlayPause.src=Pause;
 Timer = setTimeout("ChangeImage()", temps)
}

}


