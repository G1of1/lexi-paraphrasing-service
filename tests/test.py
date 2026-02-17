from fastapi.testclient import TestClient
from unittest.mock import patch, AsyncMock
from main import app

client = TestClient(app)

#Standard Paraphrase Tests
@patch("controller.controller.service.paraphrase_standard", new_callable=AsyncMock)
def test_paraphrase_standard_success(mock_detailed):

    # Mock successful service response
    mock_detailed.return_value = {
        "summary": "Mocked detailed summary"
    }

    response = client.post(
        "/api/v1/paraphrase-standard",
        json={"text": "Hello world"}
    )

    assert response.status_code == 200
    assert response.json() == {
        "summary": "Mocked detailed summary"
    }


@patch("controller.controller.service.paraphrase_standard", new_callable=AsyncMock)
def test_paraphrase_standard_error(mock_detailed):

    # Mock service returning an error
    mock_detailed.return_value = {
        "error": "Invalid input"
    }

    response = client.post(
        "/api/v1/paraphrase-standard",
        json={"text": "Hello world"}
    )

    assert response.status_code == 400
    assert response.json() == {
        "error": "Invalid input"
    }

#Simple Paraphrase Tests
@patch("controller.controller.service.paraphrase_simplify", new_callable=AsyncMock)
def test_paraphrase_simplify_success(mock_bullet):

    # Mock successful service response
    mock_bullet.return_value = {
        "summary": "Mocked bullet points summary"
    }

    response = client.post(
        "/api/v1/paraphrase-simplify",
        json={"text": "Hello world"}
    )

    assert response.status_code == 200
    assert response.json() == {
        "summary": "Mocked bullet points summary"
    }


@patch("controller.controller.service.paraphrase_simplify", new_callable=AsyncMock)
def test_paraphrase_simplify_error(mock_bullet):

    # Mock service returning an error
    mock_bullet.return_value = {
        "error": "Invalid input"
    }

    response = client.post("/api/v1/paraphrase-simplify", json={"text": "Hello world"})

    assert response.status_code == 400
    assert response.json() == {
        "error": "Invalid input"
    }



#TLDR Summarization Tests
@patch("controller.controller.service.paraphrase_shorten", new_callable=AsyncMock)
def test_paraphrase_shorten_success(mock_tldr):

    # Mock successful service response
    mock_tldr.return_value = {
        "summary": "Mocked tldr summary"
    }

    response = client.post("/api/v1/paraphrase-shorten", json={"text": "Hello world"})

    assert response.status_code == 200
    assert response.json() == {
        "summary": "Mocked tldr summary"
    }


@patch("controller.controller.service.paraphrase_shorten", new_callable=AsyncMock)
def test_paraphrase_shorten_error(mock_tldr):

    # Mock service returning an error
    mock_tldr.return_value = {
        "error": "Invalid input"
    }
    response = client.post("/api/v1/paraphrase-shorten", json={"text": "Hello world"})

    assert response.status_code == 400
    assert response.json() == {
        "error": "Invalid input"
    }

#Expand Paraphrase Tests
@patch("controller.controller.service.paraphrase_expand", new_callable=AsyncMock)
def test_paraphrase_expand_success(mock_study_notes):

    # Mock successful service response
    mock_study_notes.return_value = {
        "summary": "Mocked study notes summary"
    }

    response = client.post("/api/v1/paraphrase-expand", json={"text": "Hello world"})

    assert response.status_code == 200
    assert response.json() == {
        "summary": "Mocked study notes summary"
    }


@patch("controller.controller.service.paraphrase_expand", new_callable=AsyncMock)
def test_paraphrase_expand_error(mock_study_notes):

    # Mock service returning an error
    mock_study_notes.return_value = {
        "error": "Invalid input"
    } 

    response = client.post('/api/v1/paraphrase-expand', json={"text": "Hello world"})

    assert response.status_code == 400
    assert response.json() == {
        "error": "Invalid input"
    }

#Academic Paraphrase Tests
@patch("controller.controller.service.paraphrase_academic", new_callable=AsyncMock)
def test_paraphrase_academic_success(mock_simplification):

    # Mock successful service response
    mock_simplification.return_value = {
        "summary": "Mocked simplification summary"
    }

    response = client.post("/api/v1/paraphrase-academic", json={"text": "Hello world"})

    assert response.status_code == 200
    assert response.json() == {
        "summary": "Mocked simplification summary"
    }


@patch("controller.controller.service.paraphrase_academic", new_callable=AsyncMock)
def test_paraphrase_academic_error(mock_simplification):

    # Mock service returning an error
    mock_simplification.return_value = {
        "error": "Invalid input"
    } 

    response = client.post('/api/v1/paraphrase-academic', json={"text": "Hello world"})

    assert response.status_code == 400
    assert response.json() == {
        "error": "Invalid input"
    } 


#Formal Paraphrase Tests
@patch("controller.controller.service.paraphrase_formal", new_callable=AsyncMock)
def test_paraphrase_formal_success(mock_simplification):

    # Mock successful service response
    mock_simplification.return_value = {
        "summary": "Mocked simplification summary"
    }

    response = client.post("/api/v1/paraphrase-formal", json={"text": "Hello world"})

    assert response.status_code == 200
    assert response.json() == {
        "summary": "Mocked simplification summary"
    }


@patch("controller.controller.service.paraphrase_formal", new_callable=AsyncMock)
def test_paraphrase_formal_error(mock_simplification):

    # Mock service returning an error
    mock_simplification.return_value = {
        "error": "Invalid input"
    } 

    response = client.post('/api/v1/paraphrase-formal', json={"text": "Hello world"})

    assert response.status_code == 400
    assert response.json() == {
        "error": "Invalid input"
    } 

