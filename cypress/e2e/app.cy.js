describe('Asistente Virtual de Psicología', () => {
  beforeEach(() => {
    cy.visit('/');
  });

  it('Carga correctamente la interfaz del chat', () => {
    cy.contains('Asistente Virtual de Psicología');
    cy.get('#userInput').should('exist');
    cy.get('button').contains('Enviar');
  });

  it('Envía un mensaje y recibe una respuesta', () => {
    const mensaje = 'Hola, quiero agendar una cita';

    cy.get('#userInput').type(mensaje);

    cy.contains('Enviar').click();

    cy.get('#chat-log').should('contain.text', mensaje);
    
    cy.get('#chat-log', { timeout: 10000 }).should('not.be.empty');
  });
});
