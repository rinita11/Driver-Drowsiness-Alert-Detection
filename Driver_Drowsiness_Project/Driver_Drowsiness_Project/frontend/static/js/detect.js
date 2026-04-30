window.onload = function(){

const video = document.getElementById("video")
const alarm = document.getElementById("alarm")

navigator.mediaDevices.getUserMedia({video:true})
.then(function(stream){
video.srcObject = stream
})

setInterval(function(){

if(video.videoWidth === 0) return

let canvas = document.createElement("canvas")

canvas.width = video.videoWidth
canvas.height = video.videoHeight

let ctx = canvas.getContext("2d")

ctx.drawImage(video,0,0)

canvas.toBlob(function(blob){

let form = new FormData()

form.append("frame",blob)

fetch("/process_frame",{

method:"POST",
body:form

})

.then(res => res.json())

.then(data => {

document.getElementById("ear").innerText = data.ear
document.getElementById("mar").innerText = data.mar
document.getElementById("status").innerText = data.message

if(data.alarm){

alarm.currentTime = 0
alarm.play()

}

})

})

},400)

}