<html>
	<head>
		<title>
			Configurar per&iacute;odo de muestreo
		</title>
	</head>

	<body>

		<center>

			<?php
				
				$min = $_GET['min'];
				$sec = $_GET['sec'];
				$ok = 1;
				$t = 0;

				if ($min >= 0) {
					$t += ((int) $min) *60;
				}

				if ((($sec > 0)||($t > 0)) && ($sec < 60)){
					$t += (int) $sec;
				}else{
					$ok = 0;
				}

				if($ok){
					$fp = fopen('delay.set', 'w');
					fwrite($fp, $t);
					fclose($fp);
					echo "Nuevo per&iacute;odo establecido: \n<b>".$t."</b> segundos";
				}else{
					echo "Formato incorrecto. Retorne para corregir los datos, por favor.";
				}

			?>

		</center>

	</body>
</html>