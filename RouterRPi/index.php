<html>
	<head>
		<title>
			Configurar per&iacute;odo de muestreo
		</title>
	</head>

	<body>

		<center>

			<h2> Per&iacute;odo de muestreo </h2>
			Valor actual: 
			<?php
				$fd = fopen('delay.set', 'r');
				$myVal = fgets($fd);
				echo "".$myVal."";
				echo " segundos <br /><br />";
			?>
			<u>Establecer nuevo valor</u>
			<br />
			MINUTOS:SEGUNDOS
			<form action = "delay.php">
				<input type = "text" name = "min" size = "1" maxlength = "3" value = "00"/> :
				<input type = "text" name = "sec" size = "1" maxlength = "2" value = "00"/> 
				<br /> <br />
				<input type = "submit" name = "sub" value = "Configurar"/>
			</form>

		</center>

	</body>
</html>
