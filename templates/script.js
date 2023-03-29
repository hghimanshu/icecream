var result;
function myFunction() {
  const form = document.getElementById('email-form');
	const v = form.value;
	const length = 10;
	const chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
	result = '';
    	for (var i = length; i > 0; --i){
 	result += chars[Math.floor(Math.random() * chars.length)];
    }
	//window.alert(v);
	//alert(result);
	
document.getElementById("demo").innerHTML = "https://www.example.com/"+result;
const thankYou = document.getElementById('thank-you');
			

const f1 = document.getElementById('f1');
f1.style.display = 'none';
thankYou.style.display = 'block';


}


  function shareOnWhatsApp(result) {
    // Replace the link below with the link you want to share on WhatsApp
    const link = "https://www.example.com/"+result;
    
    // Construct the WhatsApp share link with the link parameter
    const shareLink = `https://api.whatsapp.com/send?text=${encodeURIComponent(link)}`;
    
    // Open the WhatsApp share link in a new tab
    window.open(shareLink, "_blank");
  }

