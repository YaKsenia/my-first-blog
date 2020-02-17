
//var yPos;


function setup()
{

    createCanvas(2012, 1012);

    yPos = 120;
    xPos = 120;

    yPos2 = 1120;
    xPos2 = 2020;

    yPos3 = 1120;
    xPos3 = 0;

    yPos4 = 0;
    xPos4 = 2012;


//    ellipse(50, yPos, 20,20);
//    ellipse(50, yPos + 20, 20,20);
//    ellipse(50, yPos + 40, 20,20);
//    ellipse(50, yPos + 60, 20,20);

//    text("yPos: " + yPos, 30, yPos + 100);

}

function draw()
{
   // clear();
    background(220, 10);
    fill(250,128,114);

    ellipse(xPos+45, yPos+95, 120, 300);
    ellipse(xPos, yPos, 140, 140);
    ellipse(xPos+95, yPos, 140, 140);

    ellipse(xPos2-45, yPos2-95, 120, 300);
    ellipse(xPos2, yPos2, 140, 140);
    ellipse(xPos2-95, yPos2, 140, 140);

    ellipse(xPos3-45, yPos3-95, 120, 300);
    ellipse(xPos3, yPos3, 140, 140);
    ellipse(xPos3-95, yPos3, 140, 140);

    ellipse(xPos4-45, yPos4-95, 120, 300);
    ellipse(xPos4, yPos4, 140, 140);
    ellipse(xPos4-95, yPos4, 140, 140);

    //ellipse(xPos+45, yPos+195, 100, 100);
    xPos = xPos + 10;
    yPos = yPos + 5;

    xPos2 = xPos2 - 10;
    yPos2 = yPos2 - 5;

    xPos3 = xPos3 + 10;
    yPos3 = yPos3 - 5;

    xPos4 = xPos4 - 10;
    yPos4 = yPos4 + 5;

}



