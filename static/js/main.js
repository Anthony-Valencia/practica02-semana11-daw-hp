document.addEventListener('DOMContentLoaded',()=>{
 const menu=document.getElementById('menuButton'),nav=document.getElementById('mainNav');
 if(menu&&nav)menu.addEventListener('click',()=>{const opened=nav.classList.toggle('open');menu.setAttribute('aria-expanded',String(opened));menu.querySelector('i').className=opened?'fa-solid fa-xmark':'fa-solid fa-bars'});
 const observer=new IntersectionObserver(entries=>{entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('visible');observer.unobserve(e.target)}})},{threshold:.08});
 document.querySelectorAll('.reveal').forEach((node,index)=>{node.style.setProperty('--delay',`${Math.min(index%4*65,195)}ms`);observer.observe(node)});
 const form=document.getElementById('filterForm');if(form){const order=form.querySelector('select[name=orden]');if(order)order.addEventListener('change',()=>form.submit());}
});
