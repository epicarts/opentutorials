function LinksSetColor(color){
  // var x = document.querySelectorAll('a');
  // var i = 0
  // while(i < x.length){
  //     console.log(x[i]);
  //   x[i].style.color = color;
  //   i = i + 1
  // }
  $('a').css('color',color);// all 'a' tag control jquey
}
var Body = {
  SetColor:function(color){
    document.querySelector('body').style.color = color;
  },
  SetbackgroundColor:function(color){
    document.querySelector('body').style.backgroundColor = color;
  }
}

function nightDayHandler(self){
  var target = document.querySelector('body')
  if(self.value == 'night'){
    Body.SetbackgroundColor('black');
    Body.SetColor('white');
    self.value = 'day'

    LinksSetColor('powderblue')

  } else {
    Body.SetbackgroundColor('white');
    Body.SetColor('black');
    self.value = 'night'

    LinksSetColor('blue')

    }
  }
