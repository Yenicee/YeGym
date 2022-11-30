from registro_clientes.models import cliente

cliente(nombre="Jose", direccion="Miami 237", dni=457621).save()
cliente(nombre="Ivan", direccion="Luyano 399", dni=987621).save()
cliente(nombre="Vanesa", direccion="Jta 98", dni=557621).save()
cliente(nombre="Uder", direccion="La Prida 543", dni=217621).save()

print("Se cargo con exito clientes de prueba")

from blog.models import Post

Post(title="Mi post", short_content="un post", content="si sale todo bien esto se va a mostrar").save()

print("Se cargo con éxito los post de pruebas")







