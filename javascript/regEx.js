//Letras Maiscul

const validarMaiscula = /[A-Z]/;
// console.log(validarMaiscula.test("testando"));
// console.log(validarMaiscula.test("123"));
// console.log(validarMaiscula.test("Testando"));

//ID Maiscula no final
const regex2= /\d+ID\b/;
// console.log(regex2.test("256845ID"));
// console.log(regex2.test("1234848"));
// console.log(regex2.test("asd"));

// aceita expressao da Marca/ Marca: nomeDaMarca
const regex3 = /Marca: (Nike | Adidas | Puma | Asics)/;

console.log(regex3.test("Marca: Nike"));
console.log(regex3.test("Marca: asd"));
console.log(regex3.test("asd"));