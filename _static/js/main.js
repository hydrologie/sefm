code_show=true; 
function code_toggle() {
if (code_show){
$('div.input').hide();
value='Display code'
} else {
$('div.input').not(':first').show();
}
code_show = !code_show
} 
$( document ).ready(code_toggle);

$('div.cell.code_cell.rendered.selected').find('div.input').hide()
