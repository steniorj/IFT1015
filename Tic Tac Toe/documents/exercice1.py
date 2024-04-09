# Solution (codeBoot)

main = document.querySelector('#main')

main.innerHTML = '<h1>Bonjour!</h1>'

breakpoint()

# avec le style sur l'élément
main.innerHTML = '<h1 style="color: red"><i>Bonjour!</i></h1>'

breakpoint()

# avec un élément "style" qui donne le style de #main
main.innerHTML = '<style>#main {color: red;}</style><h1><i>Bonjour!</i></h1>'

breakpoint()

main.innerHTML = '<h1 style="background-color: pink"><i>Bonjour!</i></h1>'