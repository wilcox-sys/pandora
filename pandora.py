from googlesearch import search
import requests
import time

def verificar_url(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return True
    except:
        pass
    return False

def buscar_urls(nombre_completo, num_resultados=30):
    query = f'"{nombre_completo}"'
    print(f"\n🔍 Buscando información sobre: {query}\n")
    
    urls_validas = []

    try:
        for url in search(query, num_results=num_resultados, lang="es"):
            es_valida = verificar_url(url)
            if es_valida:
                print(f"✔️  {url}")
                urls_validas.append(url)
            else:
                print(f"❌ {url}")
            time.sleep(1)  # Respetar límites de búsqueda
    except Exception as e:
        print(f"❌ Error en la búsqueda: {e}")

    return urls_validas

def guardar_resultados(nombre, urls):
    archivo = f"resultados_{nombre.replace(' ', '_')}.txt"
    with open(archivo, 'w', encoding='utf-8') as f:
        for url in urls:
            f.write(url + "\n")
    print(f"\n💾 Resultados guardados en: {archivo}")

def main():
    nombre = input("Introduce el nombre y dos apellidos: ").strip()
    resultados = buscar_urls(nombre)
    if resultados:
        guardar_resultados(nombre, resultados)
    else:
        print("⚠️ No se encontraron resultados.")

if __name__ == "__main__":
    main()
