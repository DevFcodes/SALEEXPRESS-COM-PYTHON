//Notificações

document.addEventListener('DOMContentLoaded', () => {

    const notiBtn = document.querySelector('.noti');
    const notifi = document.querySelector('.notifi');	

	if (!notiBtn || !notifi) {
        console.error('Elemento .noti ou .notifi não encontrado.');
        return;
    }

    const toggleNotifi = (e) => {
        e.stopPropagation(); 
        
        const isHidden = getComputedStyle(notifi).display === 'none';
        
        if (isHidden) {
            notifi.style.display = 'inline-flex';
        } else {
            notifi.style.display = 'none';
        }
    };

    notiBtn.addEventListener('click', toggleNotifi);

    document.addEventListener('click', (e) => {
        if (!notifi.contains(e.target) && !notiBtn.contains(e.target)) {
            notifi.style.display = 'none';
        }	
    });
    
    notifi.addEventListener('click', (e) => {
        e.stopPropagation();
    });
});




//Banner

document.addEventListener('DOMContentLoaded', () => {

    const btnbanner = document.querySelector('.btnbanner');
    const bannerLayout = document.querySelector('.bannerLayout');	

	if (!btnbanner || !bannerLayout) {
        console.error('Elemento .btnbanner ou .bannerLayout não encontrado.');
        return;
    }

    const toggleNotifi = (e) => {

        e.stopPropagation(); 
        
        const isHidden = getComputedStyle(bannerLayout).display === 'none';
        
        if (isHidden) {

            bannerLayout.style.display = 'inline-flex';
        } else {

            bannerLayout.style.display = 'none';
        }
    };

    btnbanner.addEventListener('click', toggleNotifi);

    document.addEventListener('click', (e) => {
        if (!bannerLayout.contains(e.target) && !btnbanner.contains(e.target)) {
            bannerLayout.style.display = 'none';
        }	
    });
    
    bannerLayout.addEventListener('click', (e) => {
        e.stopPropagation();
    });
});