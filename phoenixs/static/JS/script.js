
const formattedNumbers = document.querySelectorAll('.formatted-number');
formattedNumbers.forEach((element) => {
  const number = parseInt(element.textContent);
  const formattedNumber = number.toLocaleString('en-US').replace(/,/g, '.') + ' $';
  element.textContent = formattedNumber;
});
const formattedNumbers = document.querySelectorAll('.formatted-number');
formattedNumbers.forEach((element) => {
  const number = parseInt(element.textContent);
  const formattedNumber = number.toLocaleString('en-US').replace(/,/g, '.') + ' $';
  element.textContent = formattedNumber;
});