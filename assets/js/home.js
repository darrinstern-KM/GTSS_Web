/* Homepage only: hero pause, calculator, quote form, distributor finder */
/* Pause button for the hero zoom */
var pb=document.getElementById('pause');
pb.addEventListener('click',function(){var on=document.querySelector('.hero').classList.toggle('paused');pb.setAttribute('aria-pressed',on);pb.textContent=on?'Play motion':'Pause motion';});

/* Calculator: 2.25 tons per 1,000 sq ft at 1 inch. 40 bags per ton. 40 bags per pallet. */
var area = document.getElementById('area'), depth = document.getElementById('depth'), need = document.getElementById('need');
function calc(){
  var tons = Math.max(0.5, Math.round((Number(area.value)||0) / 1000 * 2.25 * Number(depth.value) * 2) / 2); /* nearest half ton */
  var bags = Math.ceil(tons * 40), pallets = Math.ceil(bags / 40);
  document.getElementById('tons').textContent = tons;
  document.getElementById('bags').textContent = bags.toLocaleString();
  document.getElementById('pallets').textContent = pallets;
  return {tons:tons,bags:bags,pallets:pallets};
}
area.addEventListener('input',calc); depth.addEventListener('change',calc);
document.querySelectorAll('.chips button').forEach(function(b){ b.addEventListener('click',function(){ area.value=b.dataset.area; depth.value=b.dataset.depth; calc(); }); });
document.getElementById('sendcalc').addEventListener('click',function(){
  var r = calc();
  need.value = 'Infield conditioner: about ' + r.tons + ' tons (' + r.bags + ' bags, ' + r.pallets + ' pallets) for ' + area.value + ' sq ft at ' + depth.options[depth.selectedIndex].text + '.';
});
document.querySelectorAll('.card').forEach(function(c){ c.addEventListener('click',function(){ need.value = 'Please quote: ' + c.dataset.product + '. '; }); });
calc();

/* Quote form: sends the request to HubSpot. No tracking scripts are loaded. */
var HS_URL = 'https://api.hsforms.com/submissions/v3/integration/submit/22428113/eeae102b-76cf-4d4a-a297-bd196cd36e0c';
var interest = '', estimate = '';
document.querySelectorAll('.card').forEach(function(c){ c.addEventListener('click',function(){ interest = c.dataset.product; }); });
document.getElementById('sendcalc').addEventListener('click',function(){ estimate = need.value; });
var qf = document.getElementById('quoteform'), msg = document.getElementById('formmsg'), sendbtn = document.getElementById('sendbtn');
function showMsg(html){ msg.innerHTML = html; msg.hidden = false; }
qf.addEventListener('submit',function(e){
  e.preventDefault();
  var v = function(id){ return document.getElementById(id).value.trim(); };
  if (v('website')) return; /* spam trap: real people never fill this */
  var bad = qf.querySelector(':invalid');
  if (bad){ showMsg('Please complete the required fields. Check: ' + qf.querySelector('label[for="'+bad.id+'"]').firstChild.textContent.trim() + '.'); bad.focus(); return; }
  var message = v('need') + '\n\nOrganization type: ' + v('orgtype') +
    (interest ? '\nProduct interest: ' + interest : '') +
    (estimate ? '\nCalculator estimate: ' + estimate : '') +
    '\nSource page: ' + document.title +
    '\nField care tips by email: ' + (document.getElementById('optin').checked ? 'Yes' : 'No');
  var f = function(name,value){ return {objectTypeId:'0-1', name:name, value:value}; };
  var fields = [f('firstname',v('fname')), f('lastname',v('lname')), f('email',v('email')), f('company',v('org')), f('zip',v('zip')), f('message',message)];
  if (v('phone')) fields.push(f('phone',v('phone')));
  sendbtn.disabled = true; sendbtn.textContent = 'Sending...'; msg.hidden = true;
  fetch(HS_URL,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({fields:fields,context:{pageUri:location.href,pageName:document.title}})})
    .then(function(r){ if(!r.ok) throw new Error(r.status); })
    .then(function(){ qf.hidden = true; var t = document.getElementById('thanks'); t.hidden = false; t.focus(); })
    .catch(function(){
      sendbtn.disabled = false; sendbtn.textContent = 'Send my quote request';
      var mail = 'mailto:info@gametimesportssystems.com?subject=' + encodeURIComponent('Quote request from ' + v('org')) + '&body=' + encodeURIComponent(v('fname')+' '+v('lname')+'\n'+v('email')+' '+v('phone')+'\n'+v('org')+'\nZIP '+v('zip')+'\n\n'+message);
      showMsg('Sorry, that did not send. Please <a href="'+mail+'">email your request</a> or call <a href="tel:18005200512">800.520.0512</a>.');
    });
});

/* Distributor finder: lists distributors for the chosen state */
var pick = document.getElementById('statepick'), out = document.getElementById('distresults');
var ALL_STATES = {AL:'Alabama',AK:'Alaska',AZ:'Arizona',AR:'Arkansas',CA:'California',CO:'Colorado',CT:'Connecticut',DE:'Delaware',FL:'Florida',GA:'Georgia',HI:'Hawaii',ID:'Idaho',IL:'Illinois',IN:'Indiana',IA:'Iowa',KS:'Kansas',KY:'Kentucky',LA:'Louisiana',ME:'Maine',MD:'Maryland',MA:'Massachusetts',MI:'Michigan',MN:'Minnesota',MS:'Mississippi',MO:'Missouri',MT:'Montana',NE:'Nebraska',NV:'Nevada',NH:'New Hampshire',NJ:'New Jersey',NM:'New Mexico',NY:'New York',NC:'North Carolina',ND:'North Dakota',OH:'Ohio',OK:'Oklahoma',OR:'Oregon',PA:'Pennsylvania',RI:'Rhode Island',SC:'South Carolina',SD:'South Dakota',TN:'Tennessee',TX:'Texas',UT:'Utah',VT:'Vermont',VA:'Virginia',WA:'Washington',WV:'West Virginia',WI:'Wisconsin',WY:'Wyoming'};
Object.keys(ALL_STATES).sort(function(a,b){ return ALL_STATES[a] < ALL_STATES[b] ? -1 : 1; }).forEach(function(k){
  var o = document.createElement('option'); o.value = k; o.textContent = ALL_STATES[k]; pick.appendChild(o);
});
var distData = null;
var distReady = fetch('/assets/data/distributors.json').then(function(r){ return r.json(); }).then(function(d){ distData = d.distributors; }).catch(function(){});
pick.addEventListener('change',function(){ distReady.then(showDistributors); });
function showDistributors(){
  var st = pick.value; out.textContent = '';
  if (!st) return;
  if (!distData){ out.innerHTML = '<p class="none"><a class="textlink" href="/distributors/">View the full distributor list</a></p>'; return; }
  var list = distData.filter(function(d){ return d.state === st; });
  if (list.length){
    var ul = document.createElement('ul');
    list.forEach(function(d){ var li = document.createElement('li'), b = document.createElement('b'), sp = document.createElement('span'); b.textContent = d.name; sp.textContent = d.city + ', ' + d.state; li.appendChild(b); li.appendChild(sp); ul.appendChild(li); });
    out.appendChild(ul);
    var p = document.createElement('p'); p.className = 'none note'; p.textContent = 'Tell us which one you prefer in your quote request and we will connect you.'; out.appendChild(p);
  } else {
    var p2 = document.createElement('p'); p2.className = 'none'; p2.textContent = 'No distributor in ' + ALL_STATES[st] + ' yet. We ship direct to you.'; out.appendChild(p2);
  }
  var a = document.createElement('a'); a.className = 'btn dark'; a.href = '#quote'; a.style.cssText = 'width:100%;margin-top:14px'; a.textContent = 'Get a quote'; out.appendChild(a);
}
