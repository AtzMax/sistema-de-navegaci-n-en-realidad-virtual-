#include <WiFi.h>
#include <WiFiUdp.h>

const char* ssid     = "LABVR";         // ← Cambia por tu red
const char* password = "04753933";      // ← Cambia por tu contraseña

const char* udpAddress = "192.168.0.109"; // IP de la PC receptora 148.204.67.139   192.168.0.103 mi compu: 192.168.0.104 gera: 192.168.0.109
const int udpPort = 4210;

WiFiUDP udp;

const int ttpA = 15;  // GPIO TTP223 A (derecha) 
const int ttpB = 4;   // GPIO TTP223 B (izquierda)

int lastState = -1;   // Guardar último estado para no spamear

void setup() {
  Serial.begin(115200);
  pinMode(ttpA, INPUT);
  pinMode(ttpB, INPUT);

  WiFi.begin(ssid, password);
  Serial.print("Conectando a WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500); Serial.print(".");
  }

  Serial.println("\nConectado a WiFi!");
  Serial.print("IP local: "); Serial.println(WiFi.localIP());
}

void loop() {
  int derecha = digitalRead(ttpA);
  int izquierda = digitalRead(ttpB);

  // Combinar en 2 bits: (izquierda << 1) | derecha
  int estado = (izquierda << 1) | derecha;

  if (estado != lastState) {  // Solo mandar si cambió
    udp.beginPacket(udpAddress, udpPort);
    udp.print(estado);        // Manda "0", "1", "2" o "3"
    udp.endPacket();

    Serial.print("Enviado: ");
    Serial.println(estado);

    lastState = estado;
  }

  delay(50); // Anti rebote
}

