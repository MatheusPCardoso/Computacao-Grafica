//cordenadas dos pontos
var fDot = { x: 0, y: 300 }
var sDot = { x: 300, y: 400 }
var tDot = { x: 400, y: 400 }
var foDot = { x: 600, y: 300 }

function setup() {
  createCanvas(1200, 1200);//tamanho do fundo
}

function draw() {
  background(224, 255, 255); //fundo 

  if (mouseIsPressed) {//verifica se o mouse está pressionado
    if (Math.abs(fDot.x - mouseX) <= 14 && Math.abs(fDot.y - mouseY) <= 14) {//movendo o primeiro ponto
      fDot.x = mouseX
      fDot.y = mouseY
    }
    else if (Math.abs(sDot.x - mouseX) <= 14 && Math.abs(sDot.y - mouseY) <= 14) {//movendo o segundo ponto
      sDot.x = mouseX
      sDot.y = mouseY
    }
    else if (Math.abs(tDot.x - mouseX) <= 14 && Math.abs(tDot.y - mouseY) <= 14) {//movendo o terceiro ponto
      tDot.x = mouseX
      tDot.y = mouseY
    }
    else if (Math.abs(foDot.x - mouseX) <= 14 && Math.abs(foDot.y - mouseY) <= 14) { //movendo o quarto ponto
      foDot.x = mouseX
      foDot.y = mouseY
    }
  }

  stroke(0); //cor da linha e pontos
  strokeWeight(24); //tamanho do ponto
  point(fDot.x, fDot.y) //primeiro ponto
  point(sDot.x, sDot.y) //segundo ponto
  point(tDot.x, tDot.y) //terceiro ponto
  point(foDot.x, foDot.y) //quarto ponto

  strokeWeight(4)// grossura linha principal
  noFill() //retirando cor
  bezier(fDot.x, fDot.y, sDot.x, sDot.y, tDot.x, tDot.y, foDot.x, foDot.y) //curva
}