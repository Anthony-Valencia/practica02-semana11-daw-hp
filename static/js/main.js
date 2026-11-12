document.addEventListener('DOMContentLoaded',()=>{
 const menu=document.getElementById('menuButton'),nav=document.getElementById('mainNav');
 if(menu&&nav)menu.addEventListener('click',()=>{const opened=nav.classList.toggle('open');menu.setAttribute('aria-expanded',String(opened));menu.querySelector('i').className=opened?'fa-solid fa-xmark':'fa-solid fa-bars'});
 const observer=new IntersectionObserver(entries=>{entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('visible');observer.unobserve(e.target)}})},{threshold:.08});
 document.querySelectorAll('.reveal').forEach((node,index)=>{node.style.setProperty('--delay',`${Math.min(index%4*65,195)}ms`);observer.observe(node)});
 const form=document.getElementById('filterForm');if(form){const order=form.querySelector('select[name=orden]');if(order)order.addEventListener('change',()=>form.submit());}
});

// Favoritos locales: no requieren iniciar sesión ni modificar la base de datos.
document.addEventListener('DOMContentLoaded', () => {
 const key='neotech-favoritos-v1';
 let favorites=[];
 try {const stored=JSON.parse(localStorage.getItem(key)||'[]');if(Array.isArray(stored))favorites=stored.map(String);}catch(e){favorites=[];}
 const buttons=[...document.querySelectorAll('[data-favorite-id]')];
 const count=document.getElementById('favoriteCount');
 const refresh=()=>{
   if(count)count.textContent=String(favorites.length);
   buttons.forEach(btn=>{
    const active=favorites.includes(btn.dataset.favoriteId);
    btn.setAttribute('aria-pressed',String(active));
    btn.classList.toggle('is-favorite',active);
    const icon=btn.querySelector('i');
    if(icon)icon.className=active?'fa-solid fa-heart':'fa-regular fa-heart';
    const isDetail=btn.classList.contains('favorite-detail');
    if(isDetail)btn.lastChild.textContent=active?' QUITAR DE FAVORITOS':' GUARDAR EN FAVORITOS';
    else {btn.setAttribute('aria-label',active?'Quitar de favoritos':'Agregar a favoritos');btn.title=active?'Quitar de favoritos':'Guardar favorito';}
   });
 };
 buttons.forEach(btn=>btn.addEventListener('click',()=>{
  const id=btn.dataset.favoriteId;
  favorites=favorites.includes(id)?favorites.filter(item=>item!==id):[...favorites,id];
  try {localStorage.setItem(key,JSON.stringify(favorites));}catch(e){}
  refresh();
 }));
 refresh();
});
