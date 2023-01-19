def test_pingRequest(mock_backend):
    assert mock_backend.pingRequest() == 200


