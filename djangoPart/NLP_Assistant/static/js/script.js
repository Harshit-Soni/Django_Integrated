const container=document.querySelector('.container')
const text =document.querySelector('#text')
const pointer=document.querySelector('.pointer')
const gc=document.querySelector('.gradient-circle')
const totaltime=8000
const changetime=4000
// const hold=totaltime/5

BreathAnimation()

function BreathAnimation(){

  pointer.classList.toggle('toggle-pointer')
  gc.classList.toggle('toggle-gradient')
    // text.innerHTML='<p>Breath In!</p>'
    container.className='container grow'

    setTimeout(()=>{
      // text.innerText = 'hold!'
      container.className='container shrink'
      setTimeout(()=>{
        // text.innerText='Breath Out!'
        container.className='container grow'
      },changetime)
    },changetime)
}

setInterval(BreathAnimation,totaltime);
function clr() {
  if (text.innerText == 'Speak...') {
    text.innerText = 'ASK'
  }
  else {
    text.innerText = 'Speak...'
  }
}
text.onclick = clr;