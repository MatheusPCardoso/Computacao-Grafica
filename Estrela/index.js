points = 4

function setup() {
    createCanvas(720, 400);
}

function verifyPoints(){
    if (mouseX < 50) points = 3
    else if (mouseX > 50 && mouseX < 100) points = 4
    else if (mouseX > 100 && mouseX < 150) points = 5
    else if (mouseX > 150 && mouseX < 200) points = 6
    else if (mouseX > 250 && mouseX < 300) points = 7
    else if (mouseX > 350 && mouseX < 400) points = 8
    else if (mouseX > 400 && mouseX < 450) points = 9
    else if (mouseX > 450 && mouseX < 500) points = 10
    else if (mouseX > 500 && mouseX < 550) points = 11
    else if (mouseX > 550 && mouseX < 650) points = 12
    else if (mouseX > 650 && mouseX < 750) points = 13
    else if (mouseX > 750 && mouseX < 800) points = 14
    else if (mouseX > 750) points = 15
}

function draw() {
    background(102);
    verifyPoints()
    push();
    translate(window.width / 2, window.height / 2);
    
    star(0, 0, 50, 150, points);
    pop();
}

function star(x, y, r1, r2, pontos) {
    let angulo = TWO_PI / pontos;
    let meioAngulo = angulo / 2.0;
    beginShape();
    for (let a = 0; a < TWO_PI; a += angulo) {
        let sx = x + cos(a) * r2;
        let sy = y + sin(a) * r2;
        vertex(sx, sy);
        sx = x + cos(a + meioAngulo) * r1;
        sy = y + sin(a + meioAngulo) * r1;
        vertex(sx, sy);
    }
    endShape(CLOSE);
}