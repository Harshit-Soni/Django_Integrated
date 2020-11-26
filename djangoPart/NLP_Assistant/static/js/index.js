const container=document.querySelector('.container')
const text =document.querySelector('#text')
const pointer=document.querySelector('.pointer')
const gc=document.querySelector('.gradient-circle')
const brand = document.querySelector('.brand')
const assistant_function = document.querySelector('#assistant_function')
const totaltime=8000
const changetime = 4000


BreathAnimation()
function BreathAnimation(){

  pointer.classList.toggle('toggle-pointer')
  gc.classList.toggle('toggle-gradient')
    // text.innerHTML='<p>Breath In!</p>'
    container.className='container grow'

    setTimeout(()=>
    {
      // text.innerText = 'hold!'
      container.className='container shrink'
      setTimeout(()=>
      {
        // text.innerText='Breath Out!'
        container.className='container grow'
      },changetime)
    },changetime)
}

setInterval(BreathAnimation,totaltime); // ???

function clr() {
  console.log('dgvhbkv')
  if (text.innerText == 'start') {
    text.innerText = 'hello'
  }
  else {
    text.innerText = 'start'
  }
  document.querySelector('.form').submit()
  document.querySelector('.introtext').classList.add('animstart')
}
text.onclick = clr;

brand.addEventListener('click',function()
{
  if (assistant_function.style.opacity=='1')
  {
    assistant_function.style.opacity='0'
    container.style.marginTop = '5px';
  }
  else{
    assistant_function.style.opacity='1'
    container.style.marginTop = '2px';
  }
  // assistant_function.classList.toggle('try');
})
