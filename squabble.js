(() => {
  var previousPeerId = null;
  var connectedTo = {};
  var peer = new Peer();

  // Helper to set up a connection
  function setupConnection(conn) {
    var connPeer = conn.peer;

    conn.send({ message: "hi" });

    console.log(`Connected to ${connPeer}`);
    connectedTo[connPeer] = conn;

    conn.on("data", (data) => {
      console.log(`'${connPeer}' sent`, data);
    });

    conn.on("close", function () {
      console.log(`Disconnected from ${connPeer}`);
      delete connectedTo[connPeer];
    });
  }

  // Standard interface
  peer.on("open", () => {
    // Workaround for deleted peer ids
    if (peer.id === null) peer.id = previousPeerId;
    else previousPeerId = peer.id;
    console.log(`My id is ${peer.id}`);
  });

  peer.on("connection", setupConnection);

  peer.on("disconnected", () => {
    console.log("Connection lost; attempting reconnect...");
    peer.id = previousPeerId;
    peer._lastServerId = previousPeerId;
    peer.reconnect();
  });

  peer.on("close", () => {
    console.log("Connection destroyed");
    connectedTo = {};
  });

  peer.on("error", console.error);

  // Public interface
  var connectIdInput = document.getElementById("connectToId");
  window.connect = () => {
    var target = connectIdInput.value;
    console.log(`Connecting to ${target}`);
    var conn = peer.connect(target);
    conn.on("open", () => {
      setupConnection(conn);
    });
  };
})();
