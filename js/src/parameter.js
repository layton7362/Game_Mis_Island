const args = process.argv;


// Konsolenausgabe der übergebenen Argumente
console.log('Übergebene Argumente:', args);

// Beispiel: Zugriff auf das dritte Argument (Index 2)
if (args.length >= 3) {
    const thirdArgument = args[2];
    console.log('Drittes Argument:', thirdArgument);
}
