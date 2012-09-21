<?php

set_time_limit(0);

$db = mysql_connect('localhost', 'root', 'root');
mysql_select_db('bafici');

$query = "SELECT * FROM films;";
$result = mysql_query($query, $db);
while ($film = mysql_fetch_array($result, MYSQL_ASSOC)) {
    $films[] = $film;
}

foreach ($films as $film) {
    $filmId = $film['id_film'];
    $pagina = file_get_contents("http://www.bafici.gov.ar/home12/web/es/films/show/v/id/$filmId.html");  
    $paginaSplited = explode('/home12/web/es/biographies/show/v/director/', $pagina);
    $directorId = explode('.html', $paginaSplited[1]);
    $directorUrl = "http://www.bafici.gov.ar/home12/web/es/biographies/show/v/director/{$directorId[0]}.html";
    $directorPagina = file_get_contents($directorUrl);
    $directorPaginaSplited = explode('/home12/photobase/directors/', $directorPagina);
    $directorName = explode('.jpg', $directorPaginaSplited[1]);
    $directorUrl = "http://www.bafici.gov.ar/home12/photobase/directors/{$directorName[0]}.jpg";
    
    
    $tempDir = '/var/www/germanscoglio.com.ar/bafici/images/directors/temp';
    $finalDir = '/var/www/germanscoglio.com.ar/bafici/images/directors';

    $image = file_get_contents($directorUrl);

    $fp = fopen("/var/www/germanscoglio.com.ar/bafici/images/directors/$filmId.jpg", 'w');
    fwrite($fp, $image);
    fclose($fp);
}