$loop = 1
$command = 'py -2 ./csv_creator.py '

Do {
	iex "$command $loop"
	$loop = $loop + 1
	start-sleep -seconds 1789
} While ($loop -lt 49)