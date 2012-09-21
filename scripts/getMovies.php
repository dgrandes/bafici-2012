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
    $paginaSplited = explode('/home12/photobase/films/', $pagina);
    $imageName = explode('.jpg', $paginaSplited[1]);
    $url = "http://www.bafici.gov.ar/home12/photobase/films/{$imageName[0]}.jpg";

    $tempDir = '/var/www/germanscoglio.com.ar/bafici/images/films/temp';
    $finalDir = '/var/www/germanscoglio.com.ar/bafici/images/films';

    $image = file_get_contents($url);

    $fp = fopen("/var/www/germanscoglio.com.ar/bafici/images/films/$filmId.jpg", 'w');
    fwrite($fp, $image);
    fclose($fp);
}